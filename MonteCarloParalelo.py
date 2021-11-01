import random
import time
import sys
import multiprocessing
from multiprocessing import Array, Process

if len(sys.argv)>1:
    d = int(sys.argv[1]) 
else:
    d = 0

def sample(n,arr,i):
    circle_points = 0
    for j in range(n):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        origin_dist = (rand_x**2 + rand_y**2)
        
        if origin_dist <= 1:
            circle_points += 1
    #print(circle_points)
        
    #return
    arr[i] = circle_points

def mc_paralelo(n = d):
    np = multiprocessing.cpu_count()
    #n = int(sys.argv[1])
    parte = int(n/np)
    sumas = Array('i', [0] * np, lock = False)

    start=time.time()
    jobs=[]
    for i in range(np):
        p = Process(target = sample ,args=(parte,sumas,i))
        jobs.append(p)
        p.start()
    
    for job in jobs:
        job.join()

    circle_points = sum(sumas)
    #print(circle_points)
    pi = 4.0 * circle_points / n
    end = time.time()

    return pi, round((end-start)*1000,2)


if __name__=='__main__':
    pi, dif = mc_paralelo()
    print("PI ESTIMATION: ", pi)
    print("TIME: ", dif, "ms")