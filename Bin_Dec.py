n=int(input("bin number:"))    # enter any binary number
ans=0   # integer to print decimal num
p=1    # power 
while n>0:   # run while loop till num becomes zero
    Ld=n%10   # last digit(Ld) of binary number
    ans=ans+Ld*(p)  
    p=2*p        # increase the power by 2 each time.
    n=n//10     # to remove last digit
print("Decimal num:",ans)
