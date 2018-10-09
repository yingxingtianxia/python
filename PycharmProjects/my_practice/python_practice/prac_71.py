#!/usr/bin/env python
#--coding: utf8--
class Student():
    name = ''
    age = 0
    score = [None]*4

    def input(self):
        self.name = raw_input('请输入姓名：')
        self.age = int(raw_input('请输入年龄：'))
        for i in range(len(self.score)):
            self.score[i] = int(raw_input('请输入第%d科目分数：'% (i+1)))

    def output(self):
        print '姓名是%s' % self.name
        print '年龄是%s' % self.age
        for i in range(len(self.score)):
            print '第%d科目的分数是%s' % (i+1, self.score[i])

if __name__ == '__main__':
    N = 5
    studentArray = [Student()] * N
    for i in range(len(studentArray)):
        studentArray[i].input()

    for i in range(len(studentArray)):
        studentArray[i].output()