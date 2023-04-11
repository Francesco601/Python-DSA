#!/usr/bin/env Python3

from random import randint


def bubble_sort(array):

    swapped=True
    while swapped:
        swapped=False
        for i in range(len(array)-1):
            if array[i]  > array[i+1]:
              array[i],array[i+1] = array[i+1],array[i]
              swapped=True

    
ARRAY_LENGTH=1000

array=[randint(0,1000) for i in range(ARRAY_LENGTH)]

bubble_sort(array)

print(array)

