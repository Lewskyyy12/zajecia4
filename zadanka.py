import numpy as np

x = np.array([3*a for a in range(15)])
print(x)

a = np.arange(2, dtype='float')
print(a)
print(a.dtype)
b = a.astype(dtype='int64')
print(b)
print(b.dtype)

def funkcja(n):
    return np.array([np.array(a) for a in range(n)])

print(funkcja(5))
