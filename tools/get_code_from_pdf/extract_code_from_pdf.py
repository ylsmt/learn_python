#!/usr/bin/env python
# encoding: utf-8


from pdfminer.pdfparser import PDFParser, PDFDocument, PDFNoOutlines, PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTChar
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

from itertools import islice
import re


def with_pdf(pdf_doc, fn, pdf_pwd, *args):
    """Open the pdf document, and apply the function, returning the results"""
    result = None
    try:
        # open the pdf file
        fp = open(pdf_doc, 'rb')
        # create a parser object associated with the file object
        parser = PDFParser(fp)
        # create a PDFDocument object that stores the document structure
        doc = PDFDocument()
        # connect the parser and document objects
        parser.set_document(doc)
        # supply the password for initialization
        doc.set_parser(parser)
        # 提供初始化密码
        # 如果没有密码 就创建一个空的字符串
        doc.initialize(pdf_pwd)

        if doc.is_extractable:
            # apply the function and return the result
            result = fn(doc, *args)

        # close the pdf file
        fp.close()
    except IOError:
        # the file doesn't exist or similar problem
        pass
    return result


def get_contents(doc):
    """
        获取章节标题
    """

    rsrcmgr = PDFResourceManager()
    # 创建一个PDF设备对象(聚合器)
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)

    # 创建一个pdf解释器对象
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    contents = [i for i in islice(doc.get_pages(), 4, 12)]
    chapters = []
    for page in contents:
        interpreter.process_page(page)
        # 接收该页面的LTPage对象
        layout = device.get_result()

        for l in layout:
            if isinstance(l, LTTextBoxHorizontal):

                # 滤掉页眉页脚
                # if l.x0 < 80:
                    # 获取章节标题
                # print(l.get_text())
                m = re.match(r'^(\d+\.)\s.*', l.get_text())
                if m:
                    chapter = re.split('\s{2,}', m.group())[0].replace('.', '').strip()
                    chapters.append(chapter)

    """
        分章节写入文件
    """

    pages_num = [1, 37, 83, 113, 141, 175, 217, 243, 329, 397, 437, 485, 539, 565, 597, 665]
    pages_num = [i + 17 for i in pages_num]

    d = {}
    for i in range(len(pages_num) - 1):
        d[chapters[i]] = (pages_num[i], pages_num[i + 1])

    print(d)
    for chapter in d:
        code_pages = [i for i in islice(doc.get_pages(), d[chapter][0], d[chapter][1])]

        print(chapter, d[chapter][0], d[chapter][1])
        code_str = ''
        for page in code_pages:
            interpreter.process_page(page)
            layout = device.get_result()

            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    # print(x.get_text(), x.x0, x.x1, x.y0, x.y1)

                    # 找到python代码位置
                    if x.x0 > 78 and x.y0 > 52:
                        code = x.get_text()
                        code_str = code_str + '\n' * 2 + code

        # filename
        for i in range(len(chapter) - 1):
            if chapter[i] not in r'<>/\|:"*?':
                pass
            else:
                chapter = chapter[:i] + chapter[i + 1:]

        fname = r".\\python_cookbook_code\\" + chapter + '.md'
        with open(fname, 'w', encoding='utf-8') as f:
            f.write('```python')
            f.write(code_str)
            f.write('```')


if __name__ == '__main__':
    pdf_path = r"PythonCookbook3rd.pdf"

    with_pdf(pdf_path, get_contents, '')
