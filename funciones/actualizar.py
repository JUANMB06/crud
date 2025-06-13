def actualizar(personas):
    try:
        id_a_actualizar = int(input("Ingrese el ID de la persona a actualizar: "))
        for persona in personas:
            if persona["id"] == id_a_actualizar:
                nuevo_nombre = input("Nuevo nombre: ")
                nueva_edad = input("Nueva edad: ")
                persona["nombre"] = nuevo_nombre
                persona["edad"] = nueva_edad
                print("Persona actualizada correctamente.\n")
                return
        print("Persona no encontrada.\n")
    except ValueError:
        print("ID inválido.\n")
