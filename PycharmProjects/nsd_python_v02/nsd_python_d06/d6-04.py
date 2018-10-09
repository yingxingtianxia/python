#！/usr/bin/env python3
#--*--coding: utf8--*--
try:
    number = int(input('请输入数字：'))
    result = 100 / number

except (ValueError, ZeroDivisionError) as reason:
    print('Error: ', reason)
except (KeyboardInterrupt, EOFError):
    print('Bye')
else:
    print(result)
finally:
    print('done')