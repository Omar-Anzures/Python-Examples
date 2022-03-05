""" Escribir una función que calcule el máximo común divisor de dos números y 
otra que calcule el mínimo común múltiplo.  """


def mcd(n, m):
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(15,20))  
print(mcm(15,20))  
