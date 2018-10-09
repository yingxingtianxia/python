#!/usr/bin/env python3
#--*--coding: utf8--*--
try:
    num = int(input('请输入：'))
    result = 100 / num

except ValueError:
    print('请输入数字')
except ZeroDivisionError:
    print('不可以使用0')
except (KeyboardInterrupt, EOFError):
    print('\n拜拜')
else:
    print(result)
finally:
    print('完成')