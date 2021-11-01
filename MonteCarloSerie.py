import random
import sys
import time

if __name__ == "__main__":

    interval = int(sys.argv[1])
    circle_points = 0

    start = time.time()

    for i in range(interval):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        origin_dist = (rand_x**2 + rand_y**2) ** 0.5

        if origin_dist <= 1:
            circle_points += 1

    pi = 4 * circle_points / interval

    end = time.time()

    # ESTIMACIÓN FINAL.

    print("PI ESTIMATION: ", pi)
    print("TIME: ", end-start)
