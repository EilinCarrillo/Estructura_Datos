def agregar(lista, numero):
    lista.append(numero)

def eliminar_ini(lista):
    if len(lista) > 0:
        lista.pop()
    else:
        print("La lista está vacía; no hay elementos para eliminar.")

def eliminar():
    lista_numeros = []
    
    while True:
        print("\n--- Menú de opciones ---")
        print("1. Agregar un número")
        print("2. Eliminar número")
        print("3. Salir")
        
        opcion = input("Elige una opción (1/2/3): ")
        
        if opcion == "1":
            # Pedir un número y agregarlo a la lista
            try:
                numero = int(input("Ingresa un número: "))
                agregar(lista_numeros, numero)
                print(f"Se agregó {numero}. Lista actual: {lista_numeros}")
            except ValueError:
                print("Por favor, ingresa un valor numérico válido.")
        
        elif opcion == "2":
            # Eliminar el último número de la lista
            eliminar_ini(lista_numeros)
            print(f"Lista actual: {lista_numeros}")
        
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

def main():
    # Llamamos a la función 'eliminar' para iniciar el proceso
    eliminar()

if __name__ == "__main__":  
    main()