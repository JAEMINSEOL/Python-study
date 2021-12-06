# -*- coding: utf-8 -*-
"""
Numpy learning

2021.12.06
"""

import numpy as np

a=[1,2,3,4,5] # List 선언
type(a)

b=np.array([1,2,3,4,0.5])
c=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[10,20,30,40,50],[60,70,80,90,100]]])

c.ndim
d=np.sqrt(c[1,1,3])

e=c.shape

f=d.dtype
d.itemsize
d.data

d=np.zeros((3,2))

e=np.arange(10,40,3)
f=np.linspace(3,8,20)

g=np.reshape(e,(2,5))

h=np.sin(g)*-g

i=h @ g.T

j=i.dot(h)

a=np.arange(2,6).reshape(2,2)
a1=a.cumsum()
a2=a.sum(axis=1).T

b=a%2==1
b = g[a%2==1,:]

data=np.random.randn(3,5)
data[data[:,0]<0,2:4]=0
data2=np.ceil(data,(2))
