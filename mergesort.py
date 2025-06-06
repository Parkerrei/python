def reverse(strr):
    if len(strr)  == 0:
        return strr 
    else: 
        return reverse(strr[1:]) + strr[0]
strr = 'mango' 
print(reverse(strr))   

