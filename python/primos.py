import math

def calculaPrimos(n):
    if n > 1:
        for i in range(2,n):
            divisores = 0
            for j in range(2,n):
                if i%j == 0:
                    divisores += 1
            if divisores == 1:
                primos.append(i)
        return primos
    return n

primos = []
n = int(input())
print(calculaPrimos(n))