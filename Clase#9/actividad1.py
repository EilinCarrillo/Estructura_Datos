class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, valor)

        return nodo

    def imprimir_por_niveles(self):
        if not self.raiz:
            print("El árbol está vacío.")
            return

        from collections import deque
        cola = deque()
        cola.append(self.raiz)

        while cola:
            nivel_actual = len(cola)
            while nivel_actual > 0:
                nodo = cola.popleft()
                print(nodo.valor, end=" ")
                if nodo.izquierdo:
                    cola.append(nodo.izquierdo)
                if nodo.derecho:
                    cola.append(nodo.derecho)
                nivel_actual -= 1
            print()  

arbol = ArbolBinario()
valores = [20, 10, 30, 5, 15, 25, 35]
for v in valores:
    arbol.insertar(v)


print("Árbol binario por niveles:")
arbol.imprimir_por_niveles()
