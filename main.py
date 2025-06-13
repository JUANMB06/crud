from funciones.crear import crear
from funciones.leer import leer
from funciones.actualizar import actualizar
from funciones.eliminar import eliminar

personas = []

def menu():
    while True:
        print("===== CRUD PRIMITIVO EN PYTHON =====")
        print("1. Crear persona")
        print("2. Leer personas")
        print("3. Actualizar persona")
        print("4. Eliminar persona")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear(personas)
        elif opcion == "2":
            leer(personas)
        elif opcion == "3":
            actualizar(personas)
        elif opcion == "4":
            eliminar(personas)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

menu()
