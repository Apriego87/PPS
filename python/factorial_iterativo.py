num = int(input("Introduce un número: "))

suma = num

def calc(n,s):
    for i in range(1,n):
        s *= i
    return s

print("El factorial de", num, "es", calc(num,suma))