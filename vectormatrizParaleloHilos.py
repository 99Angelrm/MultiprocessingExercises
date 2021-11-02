import sys
import numpy as np
import os
from threading import Thread

def function(column,N):
    global A,B,C
    for row in range (N):
        C[column]+=A[row][column]*B[row]

if __name__=='__main__':
    hilos=[]
    N=int(sys.argv[1])
    np.random.seed(0)
    A=np.random.rand(N,N)
    B=np.array(np.random.rand(N))
    C=np.zeros(N)
    for column in range (N):
        hilo=Thread(target=function,args=(column,N,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()
    print(C)