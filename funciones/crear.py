personas = []

def crear(personas):
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    persona = {"id": len(personas) + 1, "nombre": nombre, "edad": edad}
    personas.append(persona)
    print("Persona agregada exitosamente.\n")
