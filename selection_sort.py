#!/usr/bin/env Python3
from random import randint

def selection_sort(nums):

    for i in range(len(nums)):
        lowest_index=i

        for j in range(i+1,len(nums)):
            if nums[j] < nums[lowest_index]:
                lowest_index=j

        nums[i],nums[lowest_index] = nums[lowest_index],nums[i]       



random_nums=[randint for i in range[len(nums))]]
selection_sort(random_nums)
print(random_nums)

         
