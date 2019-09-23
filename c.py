myfiles = open(" ")
def reverse(s): 
    return s[::-1] 
  
def rotate(s): 
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
  
ans = rotate(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 

