class TablaHash:
    def __init__(self, tamaño=10): 
        self.tamaño = tamaño
        self.tabla = [None] * tamaño
        self.contador = 0

    def agregar(self, clave: str, valor: str):
        if self.contador < self.tamaño:
            hash_clave = hash(clave) % self.tamaño  
            self.tabla[self.contador] = (clave, valor, hash_clave)
            print(f"Contacto agregado:")
            print(f"Nombre  : {clave}")
            print(f"Teléfono: {valor}")
            print(f"Hash    : {hash_clave}")
            print(f"Índice  : {self.contador}")
            self.contador += 1        
        else:
            print("No hay espacio en la tabla.")

    def buscar(self, clave: str):
        for i in range(self.tamaño):
            lista = self.tabla[i]
            if lista and lista[0] == clave:
                clave, valor, hash_clave = lista
                print(f"\nContacto encontrado:")
                print(f"Nombre  : {clave}")
                print(f"Teléfono: {valor}")
                print(f"Hash    : {hash_clave}")
                print(f"Índice  : {i}")
                return
        print("\nContacto no encontrado.")

    def eliminar(self, clave: str):
        for i in range(self.tamaño):
            lista = self.tabla[i]
            if lista and lista[0] == clave:
                self.tabla[i] = None
                print(f"\nContacto {clave} eliminado.")
                return
        print("\nContacto no encontrado.")

    def listar(self):
        contactos = [lista for lista in self.tabla if lista]
        if contactos:
            print("\nLista de contactos:")
            for clave, valor, _ in contactos:
                print(f"{clave}: {valor}")
        else:
            print("\nNo hay contactos guardados.")


tabla = TablaHash()

while True:
    opcion = input("\nSeleccione una opción: agregar, buscar, eliminar, listar, salir: ").lower()
    if opcion == 'salir':
        break
    elif opcion == 'agregar':
        nombre = input("Digite el nombre del contacto: ")
        telefono = input("Digita el número de teléfono: ")
        tabla.agregar(nombre, telefono)
    elif opcion == 'buscar':
        nombre_buscar = input("Digite el nombre del contacto a buscar: ")
        tabla.buscar(nombre_buscar)
    elif opcion == 'eliminar':
        nombre_eliminar = input("Digite el nombre del contacto a eliminar: ")
        tabla.eliminar(nombre_eliminar)
    elif opcion == 'listar':
        tabla.listar()
    else:
        print("Opción no válida.")