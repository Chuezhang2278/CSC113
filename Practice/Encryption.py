import math

def encryption(s):
    x = math.sqrt(len(s))
    y = math.floor(x) # column
    z = math.ceil(x) # row
    
    if((y * z) < len(s)):
        y += 1
        
    final = ""
    
    for i in range(z):
        print(i)
        j = 0
        while j < z:
            if(i+z*j < len(s)):
                final += s[(i+z*j)]
            j += 1
            
        final += " "
                
    print(final)

x = "chillout"
encryption(x)