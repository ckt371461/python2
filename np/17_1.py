import numpy as np
a=np.array([1,2,3])
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])
a[0]=10
print(a[0],a[1],a[2])
b=np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b)
c=np.zeros((2,2))
print(c)
d=np.ones((1,2))
print(d)
e=np.full((2,2),7)
print(e)
f=np.eye(3)
print(f)
g=np.random.random((2,2))
print(g)