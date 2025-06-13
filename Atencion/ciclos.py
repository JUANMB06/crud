# =======================
# Ciclo FOR con rango
# =======================
print("== Ciclo for con range ==")
for i in range(5):
    print("Número:", i)

# =======================
# Ciclo FOR en lista
# =======================
print("\n== Ciclo for en lista ==")
frutas = ["manzana", "banana", "uva"]
for fruta in frutas:
    print("Fruta:", fruta)

# =======================
# FOR con índice (enumerate)
# =======================
print("\n== Ciclo for con enumerate ==")
for indice, valor in enumerate(frutas):
    print(f"Índice {indice}: {valor}")

# =======================
# Ciclo WHILE simple
# =======================
print("\n== Ciclo while simple ==")
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1

# =======================
# WHILE con condición de parada
# =======================
print("\n== Ciclo while con condición de entrada del usuario ==")
while True:
    entrada = input("Escriba 'salir' para terminar: ")
    if entrada == "salir":
        break
    print("Usted escribió:", entrada)

# =======================
# Uso de break en for
# =======================
print("\n== Uso de break en for ==")
for i in range(10):
    if i == 5:
        print("¡Se encontró el 5! Rompiendo ciclo.")
        break
    print("i:", i)

# =======================
# Uso de continue
# =======================
print("\n== Uso de continue ==")
for i in range(5):
    if i == 2:
        print("Saltando el 2")
        continue
    print("i:", i)

# =======================
# Uso de else en for
# =======================
print("\n== Uso de else con for ==")
for i in range(3):
    print("Valor:", i)
else:
    print("El ciclo for terminó sin interrupciones.")

# =======================
# Uso de else en while
# =======================
print("\n== Uso de else con while ==")
n = 0
while n < 3:
    print("n:", n)
    n += 1
else:
    print("El ciclo while terminó normalmente.")

# =======================
# Bucles anidados
# =======================
print("\n== Bucles anidados ==")
for i in range(3):
    for j in range(2):
        print(f"Par ({i}, {j})")

# =======================
# Ciclo inverso con range
# =======================
print("\n== Ciclo for inverso con range ==")
for i in range(5, 0, -1):
    print(i)
