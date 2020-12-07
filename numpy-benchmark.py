import numpy as np
import time
import sys


def main(x):
    n = np.array(x)
    X = np.ones(n, dtype=np.float)
    Y = np.ones(n, dtype=np.float)
    X += Y;
    X += Y


if __name__ == "__main__":
    if len(sys.argv) == 2:
        before = time.time()
        main(int(sys.argv[1]))# 100000000
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
        main(int(sys.argv[1]))
        # code goes here
        after = time.time()
        measurement = (after - before) * 1000
        print(measurement)
        executionTimes.append(measurement)
