#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import numpy as np
from multiprocessing import shared_memory,Process

def run(element):
    global A,B,C
    C+=A[element]*B[element]


if __name__ == "__main__":
    N= int(sys.argv[1])
    A=np.random.randint(10, size=N)
    B=np.random.randint(10, size=N)
    ptr = shared_memory.SharedMemory(name='C', create=True,size=A.nbytes)
    C=np.ndarray(1,dtype=np.float64,buffer=ptr.buf)
    jobs=[]
    for element in range(0,len(A)):
        p=Process(target=run,args=(element,))
        jobs.append(p)
        p.start()

    for p in jobs:
        p.join()
    print(A)
    print(B)
    print(C)
    ptr.unlink()
    ptr.close()