def fDecoradora(f):
    print("Soy el decorador")
    def wrapper():
        print("Hola")
        f()
        print("Adiós")
    return wrapper

@fDecoradora
def funDecorada():
    print("Soy la función decorada")

funDecorada()