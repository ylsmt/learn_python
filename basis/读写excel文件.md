### 读写excel文件

> xlrd 读 
> xlwt 写

```python
import xlrd

book = xlrd.open_workbook('demo.xlsx')

book.sheets() # 
sheet = book.sheet_by_index(0)
# 获取第一张表
sheet.nrows  # 访问行数
sheet.ncols  # 访问列数

cell = sheet.cell(0, 0) # cell 坐标

cell.ctype
# xlrd.XL_CELL_TEXT
# xlrd.XL_CELL_NUMBER

cell.value

sheet.row      # 一行
sheet.row(1)  
sheet.row_values # 直接获取值

sheet.row_values(1)  # 

sheet.row_values(1, 1) # 跳过第一个 (rows start_clox=0, end_colx=None)

sheet.col

# 添加单元格
sheet.put_cell(rowx, colx, ctype, value, xf_index)  xf_index 字体/对齐 ..  None

```

```python
improt xlwt
wbook = xlwt.Workbook()

wsheet = wbook.add_sheet('sheet1')

wsheet.write

wbook.save('xx.xlsx')
```

```python

rbook = xlrd.opne_workbook('demo.xlsx')

rsheet = rbook.sheet_by_index(0_

nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, '总分', None)

for row in range(1,rsheet.nrows):
    t = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)
    
wbook = xlwt.Workbook()
wbook.add_sheet(rsheet.name)
wsheet = wbook.add_sheet(rsheet.name)

style = xlwt.easyxf('align: vertical center, horizontal cneter')
for r in range(rsheet.nrows):
     for c in range(rsheet.ncols):
         wsheetwrite(r, c, rsheet.cell_value(r, c), style)

wbook.save('xx.xlsx')
```