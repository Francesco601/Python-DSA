

def reverse(S,start,stop):

    if start < stop -1:
        S[start],S[stop-1] = S[stop-1],S[start]
        reverse(S,start+1,stop-1)


S=[1,3,5,6,78,23]       
print(reverse(S,0,len(S)))


