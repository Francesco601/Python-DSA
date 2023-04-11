
conversion_table={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",
                  9:"9",10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}




def dec_to_hex(dec):
    hexidecimal=""
    while dec > 0:
        rem=dec % 16
        hexidecimal= conversion_table[rem] + hexidecimal
        dec = dec // 16
  
    return hexidecimal

val=dec_to_hex(69)
print(val)
