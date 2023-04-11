
def counting_sort(collection):

    if collection==[]:
        return []

    coll_len=len(collection)
    coll_max=max(collection)
    coll_min=min(collection)

    counting_arr_length=coll_max + 1 - coll_min
    counting_arr = [0] * counting_arr_length

    
    for number in collection:
        counting_arr[number-coll_min]  += 1

    for i in range(1,counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i-1]
        
    ordered=[0] * coll_len
    

    for i in reversed(range(0,coll_len)):
        ordered[counting_arr[collection[i] - coll_min] - 1] = collection[i]
        counting_arr[collection[i] - coll_min] -= 1

    return ordered


if __name__=="__main__":
        user_input=input("Enter numbers separated by a comma: \n").strip()
        unsorted=[int(item) for item in user_input.split(",")]
        x=counting_sort(unsorted)
        print(x)   
  
    

                      
                      




         

     
        
        
    
