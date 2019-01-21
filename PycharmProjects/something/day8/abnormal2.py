#!/usr/bin/env python3
try:
    num = int(input('Entry>>'))
except (KeyboardInterrupt,EOFError) as err_rpt:
    print('Stop Program')
except ValueError as err_val:
    print('Not a num')
else:
    print(num)
finally:
    print('Bye')