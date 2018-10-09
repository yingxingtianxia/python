alist = [10, 20, 'bob', 'alice', [100, 200, 300]]
print(len(alist))
print(10 in alist)  # True
print(100 in alist) # False
print(alist[2:4])
print(alist + [1000])
# print(alist + 1000)   # Error，不能把列表和数字拼接或相加
alist[-1] = 10000   # 将alist最后一项从小列表重新赋值为10000
print(alist)
alist.append(20000)  # 向列表追加20000
print(alist)
