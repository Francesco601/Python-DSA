
from random import randint

def heapify(nums,heap_size,root_index):
    largest=root_index
    left_child=(root_index * 2) + 1
    right_child=(root_index *2) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest=left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest=right_child

    if largest != root_index:
        nums[root_index],nums[largest] = nums[largest],nums[root_index]
        heapify(nums,heap_size,largest)

def heap_sort(nums):
    n=len(nums)

    for i in range(n,-1,-1):
        heapify(nums,n,i)

    for i in range(n-1,0,-1):
        nums[i],nums[0] = nums[0],nums[i]
        heapify(nums,i,0)

ARRAY_SIZE=1000
random_nums=[randint(0,1000) for i in range(ARRAY_SIZE)]
xheap_sort(random_list_of_nums)
print(random_list_of_nums)
    
    

     
