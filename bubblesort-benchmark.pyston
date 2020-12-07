import numpy as np
import time, sys


def bubblesort(X):
    N = len(X)
    for end in range(N, 1, -1):
        for i in range(end - 1):
            cur = X[i]
            if cur > X[i + 1]:
                tmp = X[i]
                X[i] = X[i + 1]
                X[i + 1] = tmp


def do_sort(sorted):
    bubblesort(sorted)


def main(x):
    original = np.arange(0.0, 10.0, x, dtype='f4')
    shuffled = original.copy()
    np.random.shuffle(shuffled)
    sorted = shuffled.copy()
    do_sort(sorted)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        before = time.time()
        main(float(sys.argv[1])) #0.01
        after = time.time()
        measurement = (after - before) * 1000
        print(measurement)
        exit(-1)
    if len(sys.argv) < 4:
        print("I need 1) the fasta 2) the max number of iterations 3) the k 4) the CoV.")
        exit(-1)
    maxNumberIterations = int(sys.argv[2])  # 30
    k = int(sys.argv[3])  # 10
    CoV = float(sys.argv[4])  # 0.02

    executionTimes = []
    for i in range(1, maxNumberIterations):
        before = time.time()
        # code goes here
        main(float(sys.argv[1]))
        # code goes here
        after = time.time()
        measurement = (after - before) * 1000
        print(measurement)
        executionTimes.append(measurement)
