import math

def calculaFibonacci(n):
    n0 = 0
    n1 = 1
    if n > 1:
        for i in range(n-1):
            x = n0 + n1
            n0 = n1
            n1 = x
        return x
    else:
        return n
            

n = int(input())
print(calculaFibonacci(n))