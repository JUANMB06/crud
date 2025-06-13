import pandas as pd

# Crear un DataFrame a partir de un diccionario
datos = {
    "Nombre": ["Ana", "Luis", "Carlos", "Sofía", "María"],
    "Edad": [23, 35, 45, 28, 33],
    "Ciudad": ["Bogotá", "Medellín", "Cali", "Bogotá", "Cali"],
    "Ventas": [1500, 2300, 1800, 2200, 1700]
}

df = pd.DataFrame(datos)

print("== DataFrame original ==")
print(df)

# Mostrar las primeras filas
print("\n== Primeras filas con head() ==")
print(df.head(3))

# Filtrar datos: personas mayores de 30 años
print("\n== Personas mayores de 30 años ==")
print(df[df['Edad'] > 30])

# Agrupar por ciudad y sumar las ventas
print("\n== Ventas totales por ciudad ==")
print(df.groupby("Ciudad")["Ventas"].sum())

# Ordenar por edad descendente
print("\n== Ordenado por edad (descendente) ==")
print(df.sort_values("Edad", ascending=False))

# Agregar una nueva columna
df["Comisión"] = df["Ventas"] * 0.05
print("\n== Con columna de Comisión ==")
print(df)

# Describir estadísticas
print("\n== Estadísticas descriptivas ==")
print(df.describe())
