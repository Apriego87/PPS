personas = [
    {"nombre": "Ruth", "edad": "47"},
    {"nombre": "Carlos", "edad": "23"},
    {"nombre": "Javier", "edad": "48"},
]

print(personas)

def f(edad):
    return edad["edad"]

personas.sort(key = f)

print(personas)

personas.sort(key = lambda persona: persona["nombre"])