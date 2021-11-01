import sys #import sys library to input vector size via cmd
import numpy as np #import numpy library to generate randon numbers in vectors with size N 

def dotMultiplication():
    N= int(sys.argv[1]) #vectors size
    A=np.random.randint(-10,10, size=N) #create vector A with random numbers and size N
    B=np.random.randint(-10,10, size=N) #create vector B with random numbers and size N
    res=0 #declare result
    for i in range(N): #for cycle to do dot product operation
        res+=A[i]*B[i]
    #print(A)
    #print(B)
    #print(res)
    return res

if __name__ == "__main__":
    dotMultiplication()