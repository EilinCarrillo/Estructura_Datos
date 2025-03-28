from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """
    if not ticket.priority_attention and ticket.age > 60:
        ticket.priority_attention = True

    ticket.priority = 1 if ticket.priority_attention else 0

    ticket_type = ticket.type.lower()
    controller: TicketController = ticketTypes.get(ticket_type)

    if controller:
        controller.enqueue(ticket)
        print(f"Ticket añadido a la cola de {ticket_type}")
    else:
        raise ValueError(f"Tipo de atención '{ticket.type}' no válido.")