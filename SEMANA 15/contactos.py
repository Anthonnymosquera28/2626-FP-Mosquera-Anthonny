#definir

def mostrar_menu():
    print("\n===== AGENDA DE CONTACTOS =====")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Listar todos los contactos")
    print("5. Salir")

def main():
    # Creación de la colección de datos (diccionario)
    # clave = nombre, valor = número telefónico
    contactos = {}

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        # 1. Agregar contacto
        if opcion == "1":
            nombre = input("Nombre del contacto: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.")
                continue
            telefono = input("Número telefónico: ").strip()
            contactos[nombre] = telefono
            print(f"Contacto '{nombre}' agregado correctamente.")

        # 2. Buscar contacto
        elif opcion == "2":
            nombre = input("Nombre a buscar: ").strip()
            if nombre in contactos:
                print(f"{nombre}: {contactos[nombre]}")
            else:
                print(f"No se encontró el contacto '{nombre}'.")

        # 3. Eliminar contacto
        elif opcion == "3":
            nombre = input("Nombre a eliminar: ").strip()
            if nombre in contactos:
                del contactos[nombre]
                print(f"Contacto '{nombre}' eliminado.")
            else:
                print(f"No se encontró el contacto '{nombre}'.")

        # 4. Listar todos los contactos
        elif opcion == "4":
            if not contactos:
                print("La agenda está vacía.")
            else:
                print("\n--- Lista de contactos ---")
                for nombre, telefono in contactos.items():
                    print(f"{nombre}: {telefono}")

        # 5. Salir
        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
