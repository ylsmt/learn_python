1.  os.stat  fstat lstat
2.  os.path...      更简洁

> 文件类型 普通文件 链接  设备文件...

1. stat.S_ISDIR(s.st_mode)
2. stat.S_ISDIR(s.st_mode)
3. s.st_mode & stat.S_IRUESR
4. s.st_mode & stat.S_IXUSER


1. os.path.isdir()
2. os.path.islink()
3. os.path.isfile()
4. 访问权限 只能用os.stat
5. os.path.getatime()
6. os.path.getsize()