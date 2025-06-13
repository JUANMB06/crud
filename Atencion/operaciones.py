# =======================
# Operaciones Aritméticas
# =======================
a = 10
b = 3

print("== Operaciones Aritméticas ==")
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

# =========================
# Operaciones Relacionales
# =========================
print("\n== Operaciones Relacionales ==")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# ===================
# Operaciones Lógicas
# ===================
x = True
y = False

print("\n== Operaciones Lógicas ==")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# ======================
# Operaciones de Asignación
# ======================
print("\n== Operaciones de Asignación ==")
c = 5
print("c =", c)
c += 2
print("c += 2 ->", c)
c -= 1
print("c -= 1 ->", c)
c *= 3
print("c *= 3 ->", c)
c /= 2
print("c /= 2 ->", c)
c %= 2
print("c %= 2 ->", c)
c **= 3
print("c **= 3 ->", c)
c //= 2
print("c //= 2 ->", c)

# ========================
# Operaciones Bit a Bit
# ========================
d = 6  # 110
e = 3  # 011

print("\n== Operaciones Bit a Bit ==")
print("d & e:", d & e)   # 010
print("d | e:", d | e)   # 111
print("d ^ e:", d ^ e)   # 101
print("~d:", ~d)         # -7 (complemento a 2)
print("d << 1:", d << 1) # 1100 (12)
print("d >> 1:", d >> 1) # 011 (3)

# ======================
# Operaciones de Identidad
# ======================
print("\n== Operaciones de Identidad ==")
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]

print("lista1 is lista2:", lista1 is lista2)   # True
print("lista1 is lista3:", lista1 is lista3)   # False
print("lista1 == lista3:", lista1 == lista3)   # True
print("lista1 is not lista3:", lista1 is not lista3)  # True

# =======================
# Operaciones de Membresía
# =======================
print("\n== Operaciones de Membresía ==")
numeros = [1, 2, 3, 4, 5]
print("3 in numeros:", 3 in numeros)
print("6 in numeros:", 6 in numeros)
print("7 not in numeros:", 7 not in numeros)
