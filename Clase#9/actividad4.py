from actividad3 import BinarySearchTree, Hospital
import pandas as pd

def buscar_hospital(arbol: BinarySearchTree, nit_buscado: int):
    def _buscar_recursivo(nodo, nit):
        if not nodo:
            return None
        if nodo.hospital.nit == nit:
            return nodo.hospital
        elif nit < nodo.hospital.nit:
            return _buscar_recursivo(nodo.left, nit)
        else:
            return _buscar_recursivo(nodo.right, nit)

    hospital = _buscar_recursivo(arbol.root, nit_buscado)
    if hospital:
        print(f"Hospital encontrado:\nNombre: {hospital.nombre}\nSede: {hospital.sede}\nMunicipio: {hospital.municipio}")
    else:
        print("Hospital no encontrado.")


bst = BinarySearchTree()

hospitales = pd.read_csv('/workspaces/Estructura_Datos/Clase#9/Directorio_E.S.E._Hospitales_de_Antioquia_con_coordenadas_20250426.csv')
hospitales.rename(columns={
    'Número NIT': 'nit',
    'Razón Social Organización': 'nombre',
    'Nombre Sede': 'sede',
    'Nombre Municipio': 'municipio'
}, inplace=True)
hospitales['nit'] = hospitales['nit'].str.replace(',', '', regex=False).str.strip()
hospitales['nit'] = pd.to_numeric(hospitales['nit'], errors='coerce').fillna(0).astype(int)

for _, row in hospitales.iterrows():
    bst.insert(Hospital(
        nit=row['nit'],
        nombre=row['nombre'],
        sede=row['sede'],
        municipio=row['municipio']
    ))

nit_a_buscar = 891982129
if bst.root: 
    buscar_hospital(bst, nit_a_buscar)
else:
    print("El árbol está vacío. No se puede realizar la búsqueda.")
