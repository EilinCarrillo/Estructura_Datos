class NodoCelda:
    def __init__(self, valor, fila, columna):
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.siguiente = None

class NodoFila:
    def __init__(self):
        self.primera_celda = None
        self.siguiente = None

class LaberintoNodos:
    def __init__(self, matriz):
        self.primera_fila = None
        anterior_fila = None
        for i, fila in enumerate(matriz):
            nodo_fila = NodoFila()
            if not self.primera_fila:
                self.primera_fila = nodo_fila
            else:
                anterior_fila.siguiente = nodo_fila
            anterior_fila = nodo_fila

            anterior_celda = None
            for j, valor in enumerate(fila):
                nodo_celda = NodoCelda(valor, i, j)
                if not nodo_fila.primera_celda:
                    nodo_fila.primera_celda = nodo_celda
                else:
                    anterior_celda.siguiente = nodo_celda
                anterior_celda = nodo_celda

    def obtener_valor(self, fila, columna):
        f = self.primera_fila
        for _ in range(fila):
            if f is None:
                return None
            f = f.siguiente
        c = f.primera_celda
        for _ in range(columna):
            if c is None:
                return None
            c = c.siguiente
        return c.valor if c else None

class NodoPila:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class PilaNodos:
    def __init__(self):
        self.cima = None

    def push(self, valor):
        self.cima = NodoPila(valor, self.cima)

    def pop(self):
        if self.cima is None:
            return None
        valor = self.cima.valor
        self.cima = self.cima.siguiente
        return valor

    def top(self):
        return self.cima.valor if self.cima else None

    def vacia(self):
        return self.cima is None

    def to_list(self):
        resultado = []
        actual = self.cima
        while actual:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado[::-1]

def resolver_laberinto_nodos(laberinto, inicio, salida):
    filas, columnas = 5, 5  
    pila = PilaNodos()
    pila.push(inicio)
    visitado = set()

    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while not pila.vacia():
        x, y = pila.top()

        if (x, y) == salida:
            return pila.to_list()

        visitado.add((x, y))
        movido = False

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto.obtener_valor(nx, ny) != 'X' and (nx, ny) not in visitado:
                pila.push((nx, ny))
                movido = True
                break

        if not movido:
            pila.pop()

    return None

matriz = [
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'X', 'O', 'E'],
    ['X', 'O', 'O', 'O', 'X']
]

laberinto = LaberintoNodos(matriz)
inicio = (0, 0)
salida = (3, 4)

solucion = resolver_laberinto_nodos(laberinto, inicio, salida)
print("Ruta encontrada:" if solucion else "No hay solución", solucion)