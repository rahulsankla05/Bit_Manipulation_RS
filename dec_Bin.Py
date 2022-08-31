n=int(input("Decimal number:"))    # enter any binary number
ans=0   # integer to print bin num
p=1    # power 
while n>0:   # run while loop till num becomes zero
    Ld=n%2   # last digit(Ld) of binary number
    ans=ans+Ld*(p)  
    p=10*p        # increase the power by 2 each time.  
    n=n//2
print("binary number:",ans)


