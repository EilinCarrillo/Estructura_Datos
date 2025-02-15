def agregar(contactos, nombre, apellido):
    clave = f"{nombre} {apellido}"
    if clave in contactos:
        print(f"la persona '{clave}' ya existe.")
    else:
        contactos[clave] = {"nombre": nombre, "apellido": apellido}
        print(f"persona'{clave}' agregada.")


def eliminar_especifico(contactos):
    if not contactos:
        print("No hay contactos para eliminar.")
        return

    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
    apellido = input("Ingrese el apellido del contacto a eliminar: ").strip()
    clave = f"{nombre} {apellido}"
    
    if clave in contactos:
        del contactos[clave]
        print(f"Contacto '{clave}' eliminado.")
    else:
        print(f"El contacto '{clave}' no se encuentra.")


def menu():
    contactos = {}
    
    while True:
        opcion = input("\n¿Qué desea hacer? (agregar/eliminar/salir): ").lower().strip()
        
        if opcion == "agregar":
            nombre = input("Ingrese el nombre: ").strip()
            apellido = input("Ingrese el apellido: ").strip()
            agregar(contactos, nombre, apellido)
            
        elif opcion == "eliminar":
            eliminar_especifico(contactos)
            
        elif opcion == "salir":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")
        
        # Mostrar los contactos actuales
        if contactos:
            print("\nContactos actuales:")
            for clave in contactos:
                print(clave)
        else:
            print("\nNo hay contactos registrados.")


def main():
    menu()


if __name__ == "__main__":  
    main()