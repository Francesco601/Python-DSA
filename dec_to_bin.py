
def convert(dec_num):
    bin=0
    rem=i=1
    while dec_num != 0:
        rem=dec_num % 2
        dec_num //= 2
        bin += rem * i
        i *= 10
        
    print(bin)

convert(64)
convert(25)
convert(92)
convert(41)
convert(87)

 
