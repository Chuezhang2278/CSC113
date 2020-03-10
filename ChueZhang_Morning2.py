#3/10/2020
#Professor Ahmet Yuksel
#Exercise 3 

def PerfectNumber():
    print("Q1, perfect number, aliquot sum")
    while True:
        n = int(input("type 0 to quit or 1 to continue\n"))
        if(n == 0):
            break
        elif(n == 1):
            try:
                n = int(input("give me a value \n"))
                total = 0
                if n <= 0:
                    print("Error, number is 0 or below")
                    return;
                    
                for i in range(1,n-1):
                    if(n % i == 0):
                        total += i
                if(total == n):
                    print(n, "is a perfect number")
                else:
                    print(n, "is not a perfect number")
                
            except ValueError:
                print("Error: Not a number, Please enter valid number")
    
#2 find all positive integer divisors of input, interfactive loop to terminate

def PosInt():
    print("Q2, find all positive integer divisor of user input\n")
    while True:
        n = int(input("Value or type 0 to quit\n"))
        if(n == 0):
            return;
        for i in range(1,n):
            if(n % i == 0):
                print(i)

#3 Check 3 user-entered points on coord plane so see if triangle, include exception handling
#terminate on user preference

def Triangle(): #need way to break out of loop still
    print("Q3, Triangle quesiton\n")
    #A+B > C
    while True:
        n = int(input("type 0 to quit or 1 to continue\n"))
        if(n == 0):
            break
        elif(n == 1):
            try:
                a = int(input("Enter Value 1 \n"))
                b = int(input("Enter Value 2 \n"))
                c = int(input("Enter Value 3 \n"))
                    
                if(((a+b) > c) and ((b+c) > a) and ((c+a)>b)):
                    print("valid triangle \n")
                else:
                    print("invalid triangle \n ")
            except ValueError:
                print("Error: Not a number, Please enter valid number")
      
#4 prime number given range, user input termination   
def PrimeTime():
    print("Q4, Prime Number given range \n")
    while True:
        n = int(input("type 0 to quit or 1 to continue\n"))
        if(n == 0):
            break
        elif(n == 1):
            a = int(input("Enter Value 1 \n"))
            b = int(input("Enter Value 2 \n"))
            for i in range(a,b):  
                if i > 1:  
                    for j in range(2,i):
                        if (i % j) == 0:  
                            break  
                        else:  
                            print(i)  
                            break

#5 X different people, how many ways Y can they be seated on table
# !! order matters
# Without order it would be X!
#Permutation formula, n!/(n-r)!

def Permutation():
    print("Q5, X guys, Y seats, order matters\n")
    def factorial(n):
        if(n == 1 or n == 0):
            return 1
        else:
            return n * factorial(n - 1);
        
    while True:
        o = int(input("type 0 to quit or 1 to continue\n"))
        if(o == 0):
            break
        elif(o == 1):
            n = int(input("Enter Value n \n"))
            if(n <= 0):
                n = int(input("Enter Valid n greater than 0\n"))
            r = int(input("Enter Value r \n"))
            if(r > n):
                r = int(input("Enter Valid r less than n \n"))
            
            print(factorial(n)/factorial(n-r))
        
    

PerfectNumber()
PosInt()
Triangle()
PrimeTime()
Permutation()
    