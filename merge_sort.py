#|/usr/bin/env Python3

from random import randint

def merge_sort(array,left_index,right_index):
   if left_index >= right_index:
      return 


   mid=(left_index+right_index) // 2
   merge_sort(array, left_index,mid)
   merge_sort(array, mid+1,right_index)
   merge(array,left_index,right_index,mid)
 
   
def merge(array,left_index,right_index,middle):

    left_copy=array[left_index:middle+1]
    right_copy=array[middle+1:right_index+1]
    left_copy_index=right_copy_index=0
    sorted_index=left_index
    

    
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
          if left_copy[left_copy_index] <= right_copy[right_copy_index]:
              array[sorted_index] = left_copy[left_copy_index]
              left_copy_index+=1

          else:
              array[sorted_index] = right_copy[right_copy_index]
              right_copy_index+=1

          sorted_index+=1
              
    while left_copy_index < len(left_copy):
       array[sorted_index] = left_copy[left_copy_index]
       left_copy_index+=1
       sorted_index+=1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index +=1
        sorted_index+=1
              

                                                   
array=[4,88,5,32,6,12,45,1,6,71,4]

   
merge_sort(array,0,len(array)-1)

print(array)
