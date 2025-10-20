"""
from math import *
from z_1 import g
h=100
a=45
b=35
u=sqrt((g*h*tan(b**2))/(2*cos(a**2)*(1-tan(b)*tan(a))))
print(u)

from numpy import *
T=200
w=300
from z_1 import e,h,k,pi
N=2/sqrt(pi)*sqrt(h*(k*T)**(3/2))*e**(w/(k*T))*w**(T/2)
print(N)

from z_1 import g
x0=4
y0=7
V0y=0.9
V0x=12
t=0
while t<=5:
    x=x0+V0x*t
    y=y0+V0y*t-((g*t**2)/2)
    print(t, x, y, end='\n')
    t=t+1

x0=4
y0=7
V0y=0.9
V0x=12
t=0
import numpy as np
from z_1 import g
n=100
a=np.zeros((n,3))
t=np.linspace(0,5,100)
a[::,0]=np.linspace(0,5,n)
a[::,1]=x0+V0x*t
a[::,2]=y0+V0y*t-((g*t**2)/2)
print(a)
"""
from numpy import *
