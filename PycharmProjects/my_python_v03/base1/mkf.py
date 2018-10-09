#!/usr/bin/env python3
#--*--coding: utf8--*--
import os

def mkfile():
    while True:
        filename = input("请输入文件名：")
        if os.path.exists(filename):
            print("文件已存在")
            continue
        else:
            context = []
            while True:
                content = input("请输入内容（输入quit结束）：")
                if content == 'quit':
                    break
                context.append(content)
            #print(context)

            with open(filename, 'a+') as fobj:
                for line in context:
                    fobj.write(line)
                    fobj.write('\n')

    return context

if __name__ == '__main__':
    mkfile()