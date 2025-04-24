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


@app.post("/ticketCreate")
def create_ticket(ticket: Ticket):
    """
    Create a new ticket and add it to the appropriate queue.
    """

    if ticket.age > 60 and not ticket.priority_attention:
        ticket.priority_attention = True
    
    
    try:
        add_queue(ticket, ticketTypes)
        return {
            "message": "Ticket created successfully",
            "ticket_data": ticket.dict()
        }
    except ValueError as e:
        return {"error": str(e)}


@app.get("/nextTicket")
def get_next_ticket(ticket_type: str):
    """
    Get the next ticket in the queue for the specified type of attention.
    """
    controller = ticketTypes.get(ticket_type.lower())
    if not controller:
        return {"error": "Invalid ticket type"}
    
    ticket = controller.dequeue()
    if ticket:
        return {
            "message": "Next ticket retrieved successfully",
            "ticket_data": ticket
        }
    else:
        return {"message": "No pending tickets for this type"}


@app.get("/ticketList")
def list_tickets(ticket_type: str):
    """
    List all pending tickets for the specified type of attention.
    """
    controller = ticketTypes.get(ticket_type.lower())
    if not controller:
        return {"error": "Invalid ticket type"}
    
    tickets = controller.get_all()
    return {
        "message": f"Pending tickets for {ticket_type}",
        "tickets": [ticket.dict() for ticket in tickets]
    }


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
