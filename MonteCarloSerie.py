import random
import sys
import time

if len(sys.argv)>1:
    d = int(sys.argv[1]) 
else:
    d = 0

def mc_serie(n = d):
    circle_points = 0

    start = time.time()

    for i in range(n):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        origin_dist = (rand_x**2 + rand_y**2) ** 0.5

        if origin_dist <= 1:
            circle_points += 1

    pi = 4 * circle_points / n

    end = time.time()

    return pi, round((end-start)*1000,2)

if __name__ == "__main__":
    pi, dif = mc_serie()
    print("PI ESTIMATION: ", pi)
    print("TIME: ", dif, "ms")
