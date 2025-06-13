def eliminar(personas):
    try:
        id_a_eliminar = int(input("Ingrese el ID de la persona a eliminar: "))
        for i, persona in enumerate(personas):
            if persona["id"] == id_a_eliminar:
                personas.pop(i)
                print("Persona eliminada correctamente.\n")
                return
        print("Persona no encontrada.\n")
    except ValueError:
        print("ID inválido.\n")
