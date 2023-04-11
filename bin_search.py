#!/usr/bin/env Python3

def bin_search(array,low,high,x):

    if high >= low:

        mid=((low+high) // 2)

        if array[mid] == x:
           return mid
       
        elif array[mid] > x:
           return  bin_search(array,low,mid-1,x)

        else:
           return bin_search(array,mid+1,high,x)

    else:
        return -1


array=[2,56,78,34,12,8,4,63,122,66,1,3,77]
x=66


result=bin_search(array,0,len(array)-1,x)

if result != -1:
    print("Element is present at index:", str(result))
else:
    print("Element is not present")


    
    
