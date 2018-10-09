class BearToy:
    def __init__(self, size, color):  # __init__在实例化时自动调用
        self.size = size  # 实例本身默认作为第一个参数自动传入
        self.color = color

    def sing(self, song):
        print(song)

if __name__ == '__main__':
    tidy = BearToy('small', 'orange')  # 实例化对象
    print(tidy.size)
    print(tidy.color)
    tidy.sing('lalala...')
    old = BearToy('large', 'brown')
    old.sing('wowowow....')
