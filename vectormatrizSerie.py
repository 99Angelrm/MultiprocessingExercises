import numpy as np
import sys
if __name__=='__main__':
    N=int(sys.argv[1])
    np.random.seed(0)
    a=np.random.rand(N,N)
    b=np.array(np.random.rand(N))
    c=np.zeros(N)
    for column in range (N):
        for row in range (N):
            c[column]+=a[row][column]*b[row]

    print(c)