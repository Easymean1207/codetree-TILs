def recursiveDigitPowerSum(n):
    if n < 10:
        return n**2
    
    return recursiveDigitPowerSum(n//10) + (n%10)**2 

N = int(input())

print(recursiveDigitPowerSum(N))