class User(object):

    def __init__(self, number):
        self.__number = number
        self.__number_2 = 0

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def set_number_2(self, number2):
        self.__number2 = number2

    def get_number_2(self):
        return self.__number2

u = User(25)
print(u.get_number())  # 25
# 真的类似于Java的反射机制吗？
print(u._User__number) # 25
# 下面又是啥情况。。。想不明白了T_T
u.set_number_2(18)
print(u.get_number_2()) # 18
print(u._User__number_2) # 0