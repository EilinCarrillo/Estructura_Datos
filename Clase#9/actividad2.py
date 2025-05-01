class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_rec(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_rec(nodo.derecho, valor)

    
    def imprimir_por_niveles(self):
        if self.raiz is None:
            print("El árbol está vacío.")
            return

        cola = [self.raiz]

        while cola:
            siguiente_nivel = []
            for nodo in cola:
                print(nodo.valor, end=" ")
                if nodo.izquierdo:
                    siguiente_nivel.append(nodo.izquierdo)
                if nodo.derecho:
                    siguiente_nivel.append(nodo.derecho)
            print()
            cola = siguiente_nivel

def buscar(nodo, valor):
    if nodo is None:
        return False
    if nodo.valor == valor:
        return True
    elif valor < nodo.valor:
        return buscar(nodo.izquierdo, valor)
    else:
        return buscar(nodo.derecho, valor)


arbol = ArbolBinario()
valores = [20, 10, 30, 5, 15, 25, 35]

for valor in valores:
    arbol.insertar(valor)

print("Árbol por niveles:")
arbol.imprimir_por_niveles()

print("\n¿Está el 15?", buscar(arbol.raiz, 15))  
print("¿Está el 50?", buscar(arbol.raiz, 50))   



