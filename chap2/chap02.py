# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:52:58 2022

@author: wx
"""

#练习1
n=42
#42=n    cannot assign to literal
x=y=1
a=22;
#b=33:    invalid syntax
c=11.
x=2
y=3
#print(xy)    name 'xy' is not defined

#练习2
#球体体积：
import math
r=5
p=4/3*math.pi*r**3
print(p)

#书的价格
p=24.96*6/10*60+(3+(60-1)*0.75)
print(p)

#回家时间
#跑步用了多少秒
time=(8*60+15)*2+(7*60+12)*3
#print(time)
#跑步用了多少分钟
minates=int(time/60)
#print(minates)
#7点过了多少分
pasttime=52+minates-60
print(pasttime)
#答：现在是7点30分
