def listaPrimos(x, div = 1):
    if div != x-1:
        div  += 1

    if div == x-1:
        return x
    elif x % div == 0:
        return False 
    else:
        return listaPrimos(x, div)
    
def calculaPrimos(n):
    cont = 2
    primos = []
    while cont < n:
        if listaPrimos(cont):
            primos.append(cont)
        cont += 1
    return primos

n = int(input())
print(calculaPrimos(n))
