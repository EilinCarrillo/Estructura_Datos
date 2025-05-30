from sklearn.ensemble import IsolationForest
import json
import datetime
import random
import time

class Node:
    def __init__(self, date, operation_type, amount, resulting_balance):
        self.date = date
        self.operation_type = operation_type
        self.amount = amount
        self.resulting_balance = resulting_balance
        self.next = None
    
    def __str__(self):
        return f"{self.date.strftime('%d/%m/%Y %H:%M:%S')} - {self.operation_type}: ${self.amount} - Balance: ${self.resulting_balance}"

class TransactionHistory:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_transaction(self, date, operation_type, amount, resulting_balance):
        new_node = Node(date, operation_type, amount, resulting_balance)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def get_history(self):
        transactions = []
        current = self.head
        while current:
            transactions.append({
                'date': current.date.isoformat(),  
                'operation_type': current.operation_type,
                'amount': current.amount,
                'resulting_balance': current.resulting_balance
            })
            current = current.next
        return transactions

    def show_history(self):
        if self.head is None:
            print("No se registraron transacciones.")
            return
        print("\n--- Historial de Transacciones ---")
        current = self.head
        while current:
            print(current)
            current = current.next
        print("--------------------------------")

class Client:
    def __init__(self, client_id, name, initial_balance=0):
        self.client_id = client_id
        self.name = name
        self.balance = initial_balance
        self.history = TransactionHistory()
        if initial_balance > 0:
            self.history.add_transaction(
                datetime.datetime.now(),
                "Initial Balance",
                initial_balance,
                initial_balance
            )
    
    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be greater than zero."
        self.balance += amount
        self.history.add_transaction(
            datetime.datetime.now(),
            "Deposit",
            amount,
            self.balance
        )
        return True, f"Deposit of ${amount} successful. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than zero."
        if amount > self.balance:
            return False, f"Insufficient funds. Current balance: ${self.balance}"
        self.balance -= amount
        self.history.add_transaction(
            datetime.datetime.now(),
            "Withdraw",
            amount,
            self.balance
        )
        return True, f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
    
    def check_balance(self):
        self.history.add_transaction(
            datetime.datetime.now(),
            "Balance Inquiry",
            0,
            self.balance
        )
        return True, f"Current balance: ${self.balance}"
    
    def get_transaction_data(self):
        transactions = self.history.get_history()

        for tx in transactions:
            if isinstance(tx['date'], str):
                tx['date'] = datetime.datetime.fromisoformat(tx['date'])

        if len(transactions) < 2:
            return []

        data = []
        for i in range(1, len(transactions)):
            current_trans = transactions[i]
            prev_trans = transactions[i-1]
            time_between = (current_trans['date'] - prev_trans['date']).total_seconds()
            if current_trans['operation_type'] in ["Deposit", "Withdraw"]:
                data.append([
                    current_trans['amount'],
                    current_trans['resulting_balance'],
                    time_between,
                    1 if current_trans['operation_type'] == "Deposit" else 0,
                ])
        return data


    def to_dict(self):
        return {"client_id": self.client_id, "name": self.name, "balance": self.balance, "history": self.history.get_history()}

    @staticmethod
    def from_dict(data):
        client = Client(data["client_id"], data["name"], data["balance"])
        for tx in data["history"]:
            client.history.add_transaction(datetime.datetime.fromisoformat(tx["date"]), tx["operation_type"], tx["amount"], tx["resulting_balance"])
        return client

class QueueNode:
    def __init__(self, client):
        self.client = client
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def enqueue(self, client):
        new_node = QueueNode(client)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
   
    def dequeue(self):
        if self.is_empty():
            return None
        removed_client = self.front.client
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return removed_client
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self._size
    
    def show(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Clients in queue:")
        index = 1
        current = self.front
        while current:
            print(f"{index}. {current.client.name}")
            current = current.next
            index += 1

class FraudDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05, random_state=42)
        self.trained = False
   
    def train(self, transaction_data):
        if len(transaction_data) >= 5:
            self.model.fit(transaction_data)
            self.trained = True
            return True
        return False
    
    def detect_fraud(self, new_transaction):
        if not self.trained:
            return False, 0
        prediction = self.model.predict([new_transaction])[0]
        score = self.model.score_samples([new_transaction])[0]
        return prediction == -1, score

class BankATM:
    def __init__(self):
        self.clients = {}
        self.client_queue = Queue()
        self.fraud_detector = FraudDetector()
        self.fraud_dataset = []
    
    def register_client(self, client_id, name, initial_balance=0):
        if client_id in self.clients:
            return False, f"Client with ID {client_id} already exists"
        new_client = Client(client_id, name, initial_balance)
        self.clients[client_id] = new_client
        return True, f"Client {name} registered successfully with ID {client_id}"
    
    def add_client_to_queue(self, client_id):
        if client_id not in self.clients:
            return False, f"No client with ID {client_id}"
        self.client_queue.enqueue(self.clients[client_id])
        return True, f"Client {self.clients[client_id].name} added to queue"
    
    def attend_next_client(self):
        if self.client_queue.is_empty():
            return False, "No clients waiting", None
        client = self.client_queue.dequeue()
        return True, f"Attending {client.name}", client
    
    def perform_operation(self, client, operation_type, amount=0):
        result = False
        message = ""
        if operation_type == "1":
            result, message = client.deposit(amount)
        elif operation_type == "2":
            result, message = client.withdraw(amount)
        elif operation_type == "3":
            result, message = client.check_balance()
        if result and operation_type in ["1", "2"]:
            self._check_fraud(client)
        return result, message
 
    def _check_fraud(self, client):
        data = client.get_transaction_data()
        if len(data) == 0:
            return
        self.fraud_dataset.extend(data[:-1])
        if len(self.fraud_dataset) >= 10 and not self.fraud_detector.trained:
            self.fraud_detector.train(self.fraud_dataset)
        if self.fraud_detector.trained:
            is_fraud, score = self.fraud_detector.detect_fraud(data[-1])
            if is_fraud:
                print("\n¡ALERTA! Posible operación fraudulenta detectada.")
                print(f"Nivel de anomalía: {score:.4f}")
                print(f"Cliente: {client.name} (ID: {client.client_id})")
                last_transaction = client.history.tail
                print(f"Transacción sospechosa: {last_transaction}")
                print("Se recomienda verificar la identidad del cliente.\n")

    def generate_simulated_data(self, num_clients=5, num_transactions=20):
        names = ["Ana García", "Juan Pérez", "María López", "Carlos Ruiz", 
                 "Laura Torres", "Pedro Sánchez", "Sofía Martínez", "Javier Fernández"]
        for i in range(1, num_clients + 1):
            name = random.choice(names)
            balance = random.randint(1000, 10000)
            self.register_client(i, name, balance)
        for _ in range(num_transactions):
            client_id = random.randint(1, num_clients)
            client = self.clients[client_id]
            op_type = random.choices(["1", "2", "3"], weights=[0.4, 0.4, 0.2])[0]
            amount = 0
            if op_type in ["1", "2"]:
                if op_type == "1":
                    amount = random.randint(100, 2000)
                else:
                    max_withdraw = min(client.balance, 2000)
                    if max_withdraw > 100:
                        amount = random.randint(100, max_withdraw)
            self.perform_operation(client, op_type, amount)
            time.sleep(random.uniform(0.1, 0.5))
        if num_clients >= 2:
            anomalous_client = self.clients[1]
            withdraw_amount = int(anomalous_client.balance * 0.8)
            self.perform_operation(anomalous_client, "2", withdraw_amount)
            anomalous_client2 = self.clients[2]
            deposit_amount = anomalous_client2.balance * 5
            self.perform_operation(anomalous_client2, "1", deposit_amount)

    def save_clients_to_file(self, filename="clientes.json"):
        with open(filename, "w") as f:
            data = [client.to_dict() for client in self.clients.values()]
            json.dump(data, f, indent=4)

    def load_clients_from_file(self, filename="clientes.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for client_data in data:
                    client = Client.from_dict(client_data)
                    self.clients[client.client_id] = client
        except FileNotFoundError:
            print(f"No se encontró el archivo {filename}. Cargando clientes vacíos.")
            
def main_menu():
    atm = BankATM()
    atm.load_clients_from_file()
    while True:
        print("\n===== BANCOOOOOOOOOOO =====")
        print("1. Registrar nuevo cliente")
        print("2. Agregar cliente a la cola")
        print("3. Atender siguiente cliente")
        print("4. Mostrar cola de clientes")
        print("5. Mostrar todos los clientes")
        print("6. Generar datos simulados")
        print("7. Salir")
        option = input("\nSelecciona una opción: ")
        if option == "1":
            client_id = input("Ingrese el ID del cliente: ")
            name = input("Ingrese el nombre del cliente: ")
            try:
                initial_balance = float(input("Ingrese el saldo inicial: $"))
                result, message = atm.register_client(client_id, name, initial_balance)
                print(message)
            except ValueError:
                print("El saldo debe ser un valor numérico.")
        elif option == "2":
            client_id = input("Ingrese el ID del cliente para encolar: ")
            result, message = atm.add_client_to_queue(client_id)
            print(message)
        elif option == "3":
            result, message, client = atm.attend_next_client()
            if result:
                print(message)
                while True:
                    print("\n--- Operaciones disponibles ---")
                    print(f"Cliente: {client.name} (ID: {client.client_id})")
                    print("1. Hacer depósito")
                    print("2. Hacer retiro")
                    print("3. Consultar saldo")
                    print("4. Mostrar historial de transacciones")
                    print("5. Finalizar servicio")
                    operation = input("\nSelecciona una operación   : ")
                    if operation in ["1", "2"]:
                        try:
                            amount = float(input("Ingrese el monto: $"))
                            result, message = atm.perform_operation(client, operation, amount)
                            print(message)
                        except ValueError:
                            print("El monto debe ser un valor numérico.")
                    elif operation == "3":
                        result, message = atm.perform_operation(client, operation)
                        print(message)
                    elif operation == "4":
                        client.history.show_history()
                    elif operation == "5":
                        print(f"Finalizando servicio para {client.name}")
                        break
                    else:
                        print("Opción inválida.")
            else:
                print(message)
        elif option == "4":
            atm.client_queue.show()
        elif option == "5":
            if not atm.clients:
                print("No hay clientes registrados.")
            else:
                print("\n--- Clientes Registrados ---")
                for client_id, client in atm.clients.items():
                    print(f"ID: {client_id} - Nombre: {client.name} - Saldo: ${client.balance}")
        elif option == "6":
            try:
                num_clients = int(input("Número de clientes a generar (1-10): "))
                num_transactions = int(input("Número de transacciones a simular (5-50): "))
                if 1 <= num_clients <= 10 and 5 <= num_transactions <= 50:
                    print(f"Generando {num_clients} clientes y {num_transactions} transacciones aleatorias...")
                    atm.generate_simulated_data(num_clients, num_transactions)
                    print("Datos simulados generados con éxito.")
                else:
                    print("Los valores deben estar dentro de los rangos especificados.")
            except ValueError:
                print("Debes ingresar valores numéricos.")
        elif option == "7":
            atm.save_clients_to_file()
            print("Adios!!.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main_menu()
