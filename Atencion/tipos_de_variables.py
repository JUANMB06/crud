print("== Tipos de Variables en Python ==")

# ===================
# Números Enteros
# ===================
entero = 10
print("entero =", entero, "| tipo:", type(entero))

# ===================
# Números Decimales (Flotantes)
# ===================
decimal = 3.14
print("decimal =", decimal, "| tipo:", type(decimal))

# ===================
# Booleanos
# ===================
verdadero = True
falso = False
print("verdadero =", verdadero, "| tipo:", type(verdadero))
print("falso =", falso, "| tipo:", type(falso))

# ===================
# Cadenas de texto
# ===================
cadena = "Hola Mundo"
print("cadena =", cadena, "| tipo:", type(cadena))

# ===================
# Listas (mutable)
# ===================
lista = [1, 2, 3, "cuatro", True]
print("lista =", lista, "| tipo:", type(lista))

# ===================
# Tuplas (inmutable)
# ===================
tupla = (1, 2, 3)
print("tupla =", tupla, "| tipo:", type(tupla))

# ===================
# Conjuntos (Set, no repetidos)
# ===================
conjunto = {1, 2, 2, 3, 4}
print("conjunto =", conjunto, "| tipo:", type(conjunto))

# ===================
# Diccionarios (clave-valor)
# ===================
diccionario = {"nombre": "Juan", "edad": 25}
print("diccionario =", diccionario, "| tipo:", type(diccionario))

# ===================
# Ningún valor (None)
# ===================
nada = None
print("nada =", nada, "| tipo:", type(nada))

# ===================
# Bytes
# ===================
datos_bytes = b"Hola"
print("datos_bytes =", datos_bytes, "| tipo:", type(datos_bytes))

# ===================
# Conversión de tipos (casting)
# ===================
print("\n== Conversión de tipos ==")
numero_str = "123"
numero_int = int(numero_str)
print(f"'{numero_str}' convertido a entero:", numero_int)

decimal_float = float("3.14")
print(f"'3.14' convertido a float:", decimal_float)

booleano = bool(1)  # cualquier número distinto de 0 es True
print("bool(1) =", booleano)

lista_desde_tupla = list((1, 2, 3))
print("Tupla convertida a lista:", lista_desde_tupla)
