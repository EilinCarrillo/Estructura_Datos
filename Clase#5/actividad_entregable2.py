from typing import Optional
from datetime import datetime

class Tarea:
    def __init__(self, descripcion: str, prioridad: int, fecha_vencimiento: str) -> None:
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        self.next: Optional["Tarea"] = None

    def get_detalle(self) -> str:
        return f"Descripción: {self.descripcion}, Prioridad: {self.prioridad}, Vence: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

class ListaTareas:
    def __init__(self) -> None:
        self.cabeza: Optional[Tarea] = None

    def agregar(self, descripcion: str, prioridad: int, fecha_vencimiento: str) -> None:
        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        
        if self.cabeza is None or (nueva_tarea.prioridad < self.cabeza.prioridad or 
                                   (nueva_tarea.prioridad == self.cabeza.prioridad and nueva_tarea.fecha_vencimiento < self.cabeza.fecha_vencimiento)):
            nueva_tarea.next = self.cabeza
            self.cabeza = nueva_tarea
            return

        nodo_actual = self.cabeza
        while nodo_actual.next is not None and (nodo_actual.next.prioridad < nueva_tarea.prioridad or 
                                                (nodo_actual.next.prioridad == nueva_tarea.prioridad and nodo_actual.next.fecha_vencimiento < nueva_tarea.fecha_vencimiento)):
            nodo_actual = nodo_actual.next

        nueva_tarea.next = nodo_actual.next
        nodo_actual.next = nueva_tarea

    def eliminar(self, descripcion: str) -> None:
        if self.cabeza is None:
            return

        if self.cabeza.descripcion == descripcion:
            self.cabeza = self.cabeza.next
            return

        nodo_actual = self.cabeza
        while nodo_actual.next is not None:
            if nodo_actual.next.descripcion == descripcion:
                nodo_actual.next = nodo_actual.next.next
                return
            nodo_actual = nodo_actual.next

    def mostrar(self) -> None:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.get_detalle())
            nodo_actual = nodo_actual.next

    def buscar(self, descripcion: str) -> None:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.descripcion == descripcion:
                print("Tarea encontrada:", nodo_actual.get_detalle())
                return
            nodo_actual = nodo_actual.next
        print("Tarea no encontrada.")

    def completar(self, descripcion: str) -> None:
        self.eliminar(descripcion)
        print(f"Tarea '{descripcion}' marcada como completada y eliminada de la lista.")

# Ejemplo de uso
lista_tareas = ListaTareas()
lista_tareas.agregar("Terminar proyecto", 1, "2025-03-10")
lista_tareas.agregar("Comprar comida", 3, "2025-03-09")
lista_tareas.agregar("Revisión médica", 2, "2025-03-08")
lista_tareas.agregar("Enviar reporte", 1, "2025-03-08")

print("\nTareas ordenadas:")
lista_tareas.mostrar()

print("\nBuscando tarea 'Comprar comida':")
lista_tareas.buscar("Comprar comida")

print("\nCompletando tarea 'Enviar reporte':")
lista_tareas.completar("Enviar reporte")

print("\nTareas actualizadas:")
lista_tareas.mostrar()
