import sys
import numpy as np
from multiprocessing import shared_memory,Process

def function(column,N):
    global A,B,C
    for row in range (N):
        C[column]+=A[row][column]*B[row]

if __name__=='__main__':
    procesos=[]
    N=int(sys.argv[1])
    np.random.seed(0)
    A=np.random.rand(N,N)
    B=np.array(np.random.rand(N))
    ptr = shared_memory.SharedMemory(name='C', create=True,size=A.nbytes)
    C=np.ndarray(N,dtype=np.float64,buffer=ptr.buf)
    for column in range (N):
        proceso=Process(target=function,args=(column,N,))
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()
    print(C)
    ptr.unlink()
    ptr.close()