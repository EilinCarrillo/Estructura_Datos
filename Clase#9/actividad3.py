import pandas as pd 

class Hospital:
    def __init__(self, nit: int, nombre: str, sede: str, municipio: str):
        self.nit = nit
        self.nombre = nombre
        self.sede = sede
        self.municipio = municipio 

    def __str__(self):
        return f'Hospital {self.nombre} con NIT {self.nit} y sede {self.sede} en el municipio {self.municipio}'
    
class Nodo:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, hospital: Hospital):
        if not self.root:
            self.root = Nodo(hospital)
        else:
            self._insert_recursive(self.root, hospital)

    def _insert_recursive(self, current: Nodo, hospital: Hospital):
        if hospital.nit < current.hospital.nit:
            if current.left is None:
                current.left = Nodo(hospital)
            else:
                self._insert_recursive(current.left, hospital)
        elif hospital.nit > current.hospital.nit:
            if current.right is None:
                current.right = Nodo(hospital)
            else:
                self._insert_recursive(current.right, hospital)

    def in_order_traversal(self):
        print(f"{'NIT':<15}{'Nombre':<30}{'Sede':<20}{'Municipio':<20}")
        print("-" * 85)
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, current: Nodo):
        if current:
            self._in_order_recursive(current.left)
            print(f"{current.hospital.nit:<15}{current.hospital.nombre:<30}{current.hospital.sede:<20}{current.hospital.municipio:<20}")
            self._in_order_recursive(current.right)

hospitales = pd.read_csv('/workspaces/Estructura_Datos/Clase#9/Directorio_E.S.E._Hospitales_de_Antioquia_con_coordenadas_20250426.csv')

hospitales.rename(columns={
    'Número NIT': 'nit',
    'Razón Social Organización': 'nombre',
    'Nombre Sede': 'sede',
    'Nombre Municipio': 'municipio' 
}, inplace=True)


hospitales['nit'] = hospitales['nit'].str.replace(',', '', regex=False).str.strip()
hospitales['nit'] = pd.to_numeric(hospitales['nit'], errors='coerce').fillna(0).astype(int)

if hospitales.empty:
    print("Error: El archivo CSV no contiene datos o no se cargó correctamente.")
else:
    print(hospitales.columns)
    print(hospitales['nit'])

    bst = BinarySearchTree()

    for _, row in hospitales.iterrows():
        bst.insert(Hospital(
            nit=row['nit'],
            nombre=row['nombre'],
            sede=row['sede'],
            municipio=row['municipio']
        ))

    print("Hospitales ordenados por NIT:")
    bst.in_order_traversal()