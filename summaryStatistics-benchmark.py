import sys
import time
from math import sqrt
import numpy as np

def calculate_number_observation(numpy_array):
    return numpy_array.size


def calculate_arithmetic_mean(numpy_array, number_observation):
    sum_result = 0.0
    for i in range(number_observation):
        sum_result += numpy_array[i]
    return sum_result / number_observation


def calculate_median(numpy_array, number_observation):
    numpy_array.sort()
    half_position = number_observation // 2
    if not number_observation % 2:
        median = (numpy_array[half_position - 1] + numpy_array[half_position]) / 2.0
    else:
        median = numpy_array[half_position]

    return median


def calculate_sample_standard_deviation(numpy_array, number_observation, arithmetic_mean):
    sum_result = 0.0
    for i in range(number_observation):
        sum_result += pow((numpy_array[i] - arithmetic_mean), 2)

    sample_variance = sum_result / (number_observation - 1)
    return sqrt(sample_variance)


def main(numpy_array):

    n_observation = calculate_number_observation(numpy_array)
    mean = calculate_arithmetic_mean(numpy_array, n_observation)
    calculate_median(numpy_array, n_observation)
    calculate_sample_standard_deviation(numpy_array, n_observation,mean)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        before = time.time()
        one_dimensional_array = np.arange(int(sys.argv[1]), dtype=np.float64)#1000000
        main(one_dimensional_array)
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
        one_dimensional_array = np.arange(int(sys.argv[1]), dtype=np.float64)
        main(one_dimensional_array)
        # code goes here
        after = time.time()
        measurement = (after - before) * 1000
        print(measurement)
        executionTimes.append(measurement)