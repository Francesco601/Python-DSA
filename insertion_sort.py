#!/usr/bin/env Python3

from random import randint


def insertion_sort(array):

    for i in range(1,len(array)):
        key_val=array[i]

        j=i-1

        while j >= 0 and array[j] > key_val:
            array[j+1]=array[j]
            j-=1         
            array[j+1]=key_val

            
ARRAY_SIZE=1000

array=[randint(0,1000) for n  in range(ARRAY_SIZE)]

insertion_sort(array)

print(array)


