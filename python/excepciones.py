import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
    resultado = x/y
    print(f"{x} / {y} = {resultado}")
except ZeroDivisionError:
    print("Error: no se puede dividir por 0")
    sys.exit(1)
except ValueError:
    print("Error: no has introducido un dato válido.")