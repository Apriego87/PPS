num = int(input("Introduce un número: "))

def calc(n):
    if (n == 1):
        return n
    else:
        return n * calc(n-1)

print("El factorial de", num, "es", calc(num))