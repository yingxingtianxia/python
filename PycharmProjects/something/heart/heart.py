#!/usr/bin/env python3

import turtle
import datetime
import time
 
#生日快乐
#Python学习群548377875
def love():
    def func(x, y):
        main()
    turtle.title('马司令专用')
    lv=turtle.Turtle()
    lv.hideturtle()
    lv.getscreen().bgcolor('light blue')
    lv.color('yellow','red')
    lv.pensize(1)
    lv.speed(1)
    lv.up()
    lv.goto(0,-150)
    #开始画爱心
    lv.down()
    lv.begin_fill()
    lv.goto(0, -150)
    lv.goto(-175.12, -8.59)
    lv.left(140)
    pos = []
    for i in range(19):
        lv.right(10)
        lv.forward(20)
        pos.append((-lv.pos()[0], lv.pos()[1]))
    for item in pos[::-1]:
        lv.goto(item)
    lv.goto(175.12, -8.59)
    lv.goto(0, -150)
    lv.left(50)
    lv.end_fill()
    #写字
    lv.up()
    lv.goto(0, 80)
    lv.down()
    lv.write("亲爱的马司令",font=(u"方正舒体",24,"normal"),align="center")
    lv.up()
    lv.goto(0, 15)
    lv.down()
    lv.write("您受委屈了",font=(u"方正舒体",36,"normal"),align="center")
    lv.up()
    lv.goto(0, -30)
    lv.down()
    lv.write("明天下班等我，给你送礼物",font=(u"方正舒体",16,"normal"),align="center")
	
	#lv.up()
    #lv.goto(100, -210)
    #lv.down()
	
 
 
if __name__ == '__main__':
   love()
   time.sleep(5)

