def foo():
    print('in foo')
    def bar():
        print('in foo-bar')
    bar()

if __name__ == '__main__':
    # bar()  # bar是在函数内部声明的，
    # 它只有在foo处于运行状态，才可见
    foo()
    # bar()  # 仍然不可用，因为foo执行完后，运行空间被释放
