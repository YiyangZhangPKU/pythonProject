from random import randint
import cProfile
import time
import line_profiler
from sympy import ntt
import numpy as np
from decimal import Decimal

@line_profiler.profile
def TestFun(numa,safety):
    if numa == 2:
        return True
    if numa == 3 or numa == 5:
        return True
    if numa%2 == 0 or numa == 1:
        return False
    m = numa -1
    s = m
    k = 0
    while s%2 == 0:
        s //= 2
        k+=1

    for _ in range(safety):
        b = randint(2,numa-2)
        r = power(b,s,numa)
        if r%numa == 1:
            return True
        else:
            for l in range(k):
                if r%numa == numa-1:
                    return True
                else:
                    r = r*r%numa
        return False


def fun():
    start = 10**2048
    timea = time.time()
    for test in range(start,start+10000):
        print(test - start)
        m = TestFun(test,10)
        if m:
            print(test)
            hexnum = hex(test)
            print(hexnum,len(hexnum))
    print(time.time()-timea)

def power(base,exponent,mod):
    res = 1
    while exponent:
        if exponent & 1:
            res = (res*base)%mod
#            res = numpy_FFT_multiply(res,base)%mod
#        base = numpy_FFT_multiply(base,base)%mod
        base = (base*base)%mod
        exponent = exponent >> 1
    return res

def calc_all_number(D):
    result = 0
    for i in range(D.shape[0]):
        result += round(Decimal(D[i].real)) * 10 ** i
    return result
def numpy_FFT_multiply(x1_vec, x2_vec):

    x1_vec = list(map(int, list(reversed(str(x1_vec)))))
    x2_vec = list(map(int, list(reversed(str(x2_vec)))))
    extra_len = 1
    while 2 ** extra_len < len(x1_vec) + len(x2_vec):
        extra_len += 1
    N = 2 ** extra_len
    A = np.fft.fft(np.array(x1_vec + [0] * (N - len(x1_vec))))
    B = np.fft.fft(np.array(x2_vec + [0] * (N - len(x2_vec))))
    C = A * B
    D = np.fft.ifft(C)
    return calc_all_number(D)

fun()









