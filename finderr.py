import sys
import re
# 读取文件
def read_file(file):
    f = open(file,'r',encoding = 'utf-8')
    try:
        lines = f.readlines()
        return lines
    except:
        print("read error")
        return []
# 写入文件
def write_file(lines):
    f = open("./result",'w')
    for line in lines:
        f.write(line)
# 主逻辑
def handler(file):
    lines=read_file(file)
    res=[]
    enable_write = False
    for line in lines:
        if re.match(r'^error*',line):
            enable_write = True
        elif re.match(r'\n',line):
            if enable_write is True:
                res.append("\n")
            enable_write = False
        if enable_write is True:
            res.append(line)
    write_file(res)
def main():
    file=sys.argv[1]
    handler(file)
main()