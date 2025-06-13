print("== TIPOS DE DATOS EN PYTHON ==")

# ============
# Numéricos
# ============
entero = 42              # int
decimal = 3.1416         # float
complejo = 1 + 2j        # complex

print("\n== Numéricos ==")
print("Entero:", entero, type(entero))
print("Decimal:", decimal, type(decimal))
print("Complejo:", complejo, type(complejo))

# ============
# Texto
# ============
texto = "Hola, Python"   # str

print("\n== Texto ==")
print("Cadena:", texto, type(texto))

# ============
# Booleanos
# ============
activo = True
inactivo = False

print("\n== Booleanos ==")
print("Activo:", activo, type(activo))
print("Inactivo:", inactivo, type(inactivo))

# ============
# Secuencias
# ============
lista = [1, 2, 3]                  # list
tupla = (4, 5, 6)                 # tuple
rango = range(3)                 # range

print("\n== Secuencias ==")
print("Lista:", lista, type(lista))
print("Tupla:", tupla, type(tupla))
print("Rango:", list(rango), type(rango))

# ============
# Colecciones
# ============
conjunto = {1, 2, 3}              # set
diccionario = {"a": 1, "b": 2}    # dict

print("\n== Colecciones ==")
print("Conjunto:", conjunto, type(conjunto))
print("Diccionario:", diccionario, type(diccionario))

# ============
# Tipo None (ausencia de valor)
# ============
nulo = None

print("\n== NoneType ==")
print("Valor nulo:", nulo, type(nulo))

# ============
# Bytes y Bytearray
# ============
datos = b"Hola"                  # bytes
mutable = bytearray(5)          # bytearray
vista = memoryview(bytes(5))    # memoryview

print("\n== Bytes ==")
print("Bytes:", datos, type(datos))
print("Bytearray:", mutable, type(mutable))
print("Memoryview:", vista, type(vista))

# ============
# Casting de tipos
# ============
print("\n== Conversión de Tipos ==")
print("str(100):", str(100))
print("int('200'):", int("200"))
print("float(5):", float(5))
print("list('abc'):", list("abc"))
