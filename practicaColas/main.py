from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI()

ticketTypes = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

# Endpoint para crear un turno
@app.post("/ticketCreate")
def crear_turno(turno: Ticket):
    # Aquí podrías agregar la lógica para guardar el turno en una base de datos
    add_queue(turno, ticketTypes)
    return {"mensaje": "Turno creado correctamente", "datos_turno": turno}

# Endpoint para obtener el siguiente turno
def obtener_siguiente_turno(tipo: str):
    controller = ticketTypes.get(tipo.lower())
    if not controller:
        return {"mensaje": "Tipo de atención no válido"}
    
    ticket = controller.dequeue()
    if ticket:
        return {"mensaje": "El siguiente turno es", "datos_turno": ticket}
    else:
        return {"mensaje": "No hay turnos pendientes"}

# Endpoint para listar los turnos en cola por el tipo de turno
@app.get("/ticketList")
def listar_turnos_cola(tipo: str):
    controller = ticketTypes.get(tipo.lower())
    if not controller:
        return {"mensaje": "Tipo de atención no válido"}
    
    tickets = controller.get_all()
    return {"mensaje": "Lista de turnos en cola", "datos_turnos": tickets}

# Otros endpoints existentes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
