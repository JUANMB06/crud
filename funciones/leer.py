def leer(personas):
    if not personas:
        print("No hay personas registradas.\n")
    else:
        print("Listado de personas:")
        for persona in personas:
            print(f"ID: {persona['id']}, Nombre: {persona['nombre']}, Edad: {persona['edad']}")
        print()
