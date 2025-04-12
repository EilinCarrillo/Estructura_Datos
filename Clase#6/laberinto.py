def resolver_laberinto(laberinto, inicio, salida):
    filas, columnas = len(laberinto), len(laberinto[0])
    pila = [inicio]  
    visitado = set()

    while pila:
        x, y = pila[-1] 

        if (x, y) == salida:
            return pila  

        visitado.add((x, y))

        
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        movido = False

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy

            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] != 'X' and (nx, ny) not in visitado:
                pila.append((nx, ny))
                movido = True
                break  

        if not movido:  
            pila.pop()

    return None  


laberinto = [
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'X', 'O', 'E'],
    ['X', 'O', 'O', 'O', 'X']
]

inicio = (0, 0)
salida = (3, 4)

solucion = resolver_laberinto(laberinto, inicio, salida)
print("Ruta encontrada:" if solucion else "No hay solución", solucion)


def verificar_balanceo(expresion):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for simbolo in expresion:
        if simbolo in '({[':
            pila.append(simbolo)  
        elif simbolo in ')}]':
            if not pila or pila.pop() != pares[simbolo]:
                return False  

    return not pila  


expresiones = ["{[()()]}", "[(])", "{(a+b) * [c/d]}", "[{()}]", "{(a+b]}"]
for expr in expresiones:
    print(f"{expr}: {'Balanceado' if verificar_balanceo(expr) else 'No balanceado'}")
