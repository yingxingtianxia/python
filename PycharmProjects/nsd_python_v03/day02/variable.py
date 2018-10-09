# 变量使用小写字母
# 尽量使用有意义的名字pythonstring
# 尽量简短　pystr
# 多个单词间，使用下划线分开 py_str
# 类名采用骆驼样式写法 MyClass
# 变量使用名词，如phone，函数使用谓词(动词+名词)，如update_phone
# python是动态类型的语言，变量类型由它的值决定
# 变量在使用之前，必须先赋值

a = 100
a = a + 50  # 赋值自右向左，先计算a+50，把结果再赋值
a += 50     # 上面语句的简化写法

# 在python解释器中执行import this可以看到python之禅
# 美胜丑，明胜暗，简胜繁
print(5 / 2)   # 2.5
print(5 // 2)  # 2
print(5 % 2)   # 1　　求余，模运算
print(2 ** 3)  # 8    幂运算
print(3 == 3)  # 判断是否相等，返回True
print(3 != 3)  # 判断是否不相等，返回False
print(10 < 20 < 30)  # python支持连续比较
print(True and False)   # False
print(True and True)    # True
print(True or False)    # True
print(not True)         # False
