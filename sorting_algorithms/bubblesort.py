#bubble sort algorithm implementation in python

from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    
    stmt = f"{algorithm}({array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minmum execution time: {min(times)}")

def bubble_sort(array):
    n = len(array)

    for i in range(n):

        already_sorted = True

        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]

                already_sorted=False
        
        if already_sorted:
            break
    
    return array

ARRAY_LENGTH = 10

if __name__ == '__main__':
    
    array = [randint (0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm = 'bubble_sort', array=array)