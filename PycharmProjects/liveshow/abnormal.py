#!/usr/bin/env python3
try:
    num = int(input("Entry>>"))
except ValueError as err_val:
    print("not int")
except (KeyboardInterrupt, EOFError) as err_rpt:
    print("Stop")
else:
    print(num)
finally:
    print('Bye')