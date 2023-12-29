import math

def calculaFibonacci(n):
    if n <= 1:
        return n
    else:
        return(calculaFibonacci(n-1)+(calculaFibonacci(n-2)))

n = int(input())
print(calculaFibonacci(n))