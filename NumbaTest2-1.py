from math import cos, log
import numba as nb
import numpy as np
import time
import dis

def f_py(I, J):
    res = 0
    for i in range(I):
        for j in range (J):
            res += int(cos(log(1)))
    return res

def f_np(I, J):
    a = np.ones((I, J), dtype=np.float64)
    return int(np.sum(np.cos(np.log(a)))), a

I, J = 10000, 10000

# Python
start = time.time()
f_py(I, J)
print("Python time : " + str(time.time() - start) + " " + "seconds")

# Numpy
start = time.time()
res, a = f_np(I, J)
print("Numpy time : " + str(time.time() - start) + " " + "seconds")

# Numba
start = time.time()
f_nb = nb.jit(f_py)
f_nb(I, J)
print("Numba time : " + str(time.time() - start) + " " + "seconds")

dis.dis()


