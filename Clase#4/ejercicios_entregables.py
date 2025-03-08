#class Vehiculo:
   # def __init__(self, marca: str, combustible: float, tipo: str):
       # self.marca = marca
        #self.combustible = combustible
        #self.encendido = False
        #self.tipo = tipo

    #def __str__(self) -> str:
       # return f"Tipo: {self.tipo} | Marca: {self.marca} | Combustible: {self.combustible:.2f} gal"

    #def encender(self):
        #if self.combustible < 1:
           # return "Combustible bajo. Necesitas ir a la gasolinera."
        #self.encendido = True
        #return f"{self.tipo} {self.marca} ha sido encendido."

    #def arrancar(self):
        #if not self.encendido:
         #   return f"El {self.tipo.lower()} está apagado. Enciéndelo primero."
        #if self.combustible <= 0:
            #return "Combustible agotado. El vehículo se ha detenido."
        #self.combustible -= 0.5
        #if self.combustible < 1:
           # return "Advertencia: Combustible muy bajo. Ve a la gasolinera pronto."
        #return f"{self.tipo} {self.marca} está en marcha. Combustible restante: {self.combustible:.2f} gal."


#class Moto(Vehiculo):
    #def __init__(self, marca: str, combustible: float):
        #super().__init__(marca, combustible, "Moto")


#class Carro(Vehiculo):
    #def __init__(self, marca: str, combustible: float):
        #super().__init__(marca, combustible, "Carro")


#moto1 = Moto("Duke", 2.5)
#print(moto1)
#print(moto1.encender())
#print(moto1.arrancar())

#carro1 = Carro("Renault", -0.3)
#print(carro1)
#print(carro1.encender())
#print(carro1.arrancar())

#class Persona:
    #def __init__(self, nombre, edad, genero):
       # self.nombre = nombre
        #self.edad = edad
       # self.genero = genero
    
    #def obtener_datos(self):
       # return self.nombre, self.edad, self.genero
    
    #def establecer_datos(self, nombre, edad, genero):
        #self.nombre = nombre
        #self.edad = edad
        #self.genero = genero
    
    #def presentarse(self):
        #print(f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.genero}.")


#class CuentaBancaria:
   # def __init__(self, titular, saldo, numeroDeCuenta):
        #self.titular = titular
        #self.saldo = saldo
        #self.numeroDeCuenta = numeroDeCuenta
    
    #def depositar(self, cantidad):
       # self.saldo += cantidad
        #print(f"Depósito realizado. Nuevo saldo: {self.saldo}")
    
    #def retirar(self, cantidad):
        #if cantidad > self.saldo:
            #print("Fondos insuficientes.")
        #else:
            #self.saldo -= cantidad
            #print(f"Retiro realizado. Nuevo saldo: {self.saldo}")
    
    #def consultar_saldo(self):
        #print(f"Saldo actual: {self.saldo}")
       # return self.saldo


#class Rectangulo:
    #def __init__(self, base, altura):
       # self.base = base
        #self.altura = altura
    
   # def calcular_area(self):
        #area = self.base * self.altura
        #print(f"Área del rectángulo: {area}")
        #return area
    
    #def calcular_perimetro(self):
        #perimetro = 2 * (self.base + self.altura)
        #print(f"Perímetro del rectángulo: {perimetro}")
        #return perimetro


#class Circulo:
    #def __init__(self, radio):
        #self.radio = radio
    
    #def calcular_area(self):
        #area = 3.1416 * (self.radio ** 2)
        #print(f"Área del círculo: {area}")
        #return area
    
    #def calcular_circunferencia(self):
        #circunferencia = 2 * 3.1416 * self.radio
        #print(f"Circunferencia del círculo: {circunferencia}")
        #return circunferencia


#class Libro:
   # def __init__(self, titulo, autor, genero, añoDePublicacion):
        #self.titulo = titulo
        #self.autor = autor
        #self.genero = genero
        #self.añoDePublicacion = añoDePublicacion
    
    #def mostrar_detalles(self):
       # print(f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año: {self.añoDePublicacion}")


#class Cancion:
    #def __init__(self, titulo, artista, album, duracion):
       # self.titulo = titulo
        #self.artista = artista
        #self.album = album
        #self.duracion = duracion
    
    #def reproducir(self):
       # print(f"Reproduciendo: {self.titulo} - {self.artista}")


#class Producto:
    #def __init__(self, nombre, precio, cantidadDisponible):
        #self.nombre = nombre
        #self.precio = precio
        #self.cantidadDisponible = cantidadDisponible
    
    #def calcular_total(self, cantidad):
       # if cantidad <= self.cantidadDisponible:
            #total = self.precio * cantidad
            #print(f"Total a pagar por {cantidad} unidades de {self.nombre}: {total}")
            #return total
        #else:
           # print("Stock insuficiente")
            #return "Stock insuficiente"


#class Estudiante:
    #def __init__(self, nombre, edad, curso):
        #self.nombre = nombre
        #self.edad = edad
        #self.curso = curso
       # self.calificaciones = []
    
    #def agregar_calificacion(self, calificacion):
        #self.calificaciones.append(calificacion)
       # print(f"Calificación {calificacion} agregada.")
    
    #def calcular_promedio(self):
        #promedio = sum(self.calificaciones) / len(self.calificaciones) if self.calificaciones else 0
        #print(f"Promedio de {self.nombre}: {promedio}")
        #return promedio
    
    #def aprobar(self):
       # estado = "Aprobado" if self.calcular_promedio() >= 6 else "Reprobado"
        #print(f"Estado de {self.nombre}: {estado}")
        #return estado
# Crear una persona
#persona1 = Persona("Juan", 30, "Hombre")
#persona1.presentarse()  # Esto imprimirá la presentación

# Crear una cuenta bancaria
#cuenta1 = CuentaBancaria(persona1, 1000, "123456789")
#print(f"Saldo inicial: {cuenta1.consultar_saldo()}")
#cuenta1.depositar(500)
#print(f"Saldo después del depósito: {cuenta1.consultar_saldo()}")
#cuenta1.retirar(2000)  # Esto imprimirá "Fondos insuficientes"
#cuenta1.retirar(300)
#print(f"Saldo después del retiro: {cuenta1.consultar_saldo()}")

# Crear un rectángulo
#rectangulo1 = Rectangulo(5, 10)
#print(f"Área del rectángulo: {rectangulo1.calcular_area()}")
#print(f"Perímetro del rectángulo: {rectangulo1.calcular_perimetro()}")

# Crear un círculo
#circulo1 = Circulo(7)
#print(f"Área del círculo: {circulo1.calcular_area()}")
#print(f"Circunferencia del círculo: {circulo1.calcular_circunferencia()}")

# Crear un libro
#libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 1967)
#libro1.mostrar_detalles()

# Crear una canción
#cancion1 = Cancion("Bohemian Rhapsody", "Queen", "A Night at the Opera", "5:55")
#cancion1.reproducir()

# Crear un producto
#producto1 = Producto("Laptop", 1500, 5)
#print(f"Total por 3 laptops: {producto1.calcular_total(3)}")
#print(f"Total por 6 laptops: {producto1.calcular_total(6)}")  # Debería mostrar "Stock insuficiente"

# Crear un estudiante
#estudiante1 = Estudiante("Ana", 20, "Matemáticas")
#estudiante1.agregar_calificacion(8)
#estudiante1.agregar_calificacion(9)
#estudiante1.agregar_calificacion(7)
#print(f"Promedio de {estudiante1.nombre}: {estudiante1.calcular_promedio()}")
#print(f"Estado: {estudiante1.aprobar()}")

class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def obtener_datos(self):
        return self.nombre, self.edad, self.genero
    
    def establecer_datos(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.genero}.")


class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def trabajar(self):
        print(f"{self.nombre} está trabajando en el departamento de {self.departamento}.")

    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo
    
    def trabajar(self):
        print(f"{self.nombre} está supervisando a su equipo de {len(self.equipo)} empleados.")

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguajeDeProgramacion):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion
    
    def trabajar(self):
        print(f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}.")


class FiguraGeometrica:
    def calcular_area(self):
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        area = (self.base * self.altura) / 2
        print(f"Área del triángulo: {area}")
        return area

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        area = self.lado ** 2
        print(f"Área del cuadrado: {area}")
        return area


class Electrodomestico:
    def __init__(self, marca, modelo, consumoEnergetico):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergetico = consumoEnergetico
    
    def encender(self):
        print(f"El electrodoméstico {self.marca} {self.modelo} está encendido.")
    
    def mostrar_informacion(self):
        print(f"Electrodoméstico: {self.marca} {self.modelo}, Consumo Energético: {self.consumoEnergetico}")

class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergetico, capacidad):
        super().__init__(marca, modelo, consumoEnergetico)
        self.capacidad = capacidad
    
    def encender(self):
        print(f"La lavadora {self.marca} {self.modelo} ha iniciado el ciclo de lavado con capacidad de {self.capacidad} kg.")

class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergetico, tieneCongelador):
        super().__init__(marca, modelo, consumoEnergetico)
        self.tieneCongelador = tieneCongelador
    
    def encender(self):
        congelador = "con congelador" if self.tieneCongelador else "sin congelador"
        print(f"El refrigerador {self.marca} {self.modelo} está regulando la temperatura {congelador}.")


class Usuario:
    def __init__(self, nombreDeUsuario, contraseña):
        self.nombreDeUsuario = nombreDeUsuario
        self.contraseña = contraseña
    
    def iniciar_sesion(self, usuario, contraseña):
        if usuario == self.nombreDeUsuario and contraseña == self.contraseña:
            print("Inicio de sesión exitoso.")
        else:
            print("Credenciales incorrectas.")
    
    def mostrar_informacion(self):
        print(f"Usuario: {self.nombreDeUsuario}")

class Administrador(Usuario):
    def gestionar_usuarios(self):
        print(f"{self.nombreDeUsuario} está gestionando usuarios.")

class Cliente(Usuario):
    def realizar_compra(self):
        print(f"{self.nombreDeUsuario} ha realizado una compra.")

# Pruebas con datos
persona1 = Persona("Juan", 30, "Hombre")
persona1.presentarse()


empleado1 = Empleado("Ana", 5000, "Ventas")
empleado1.mostrar_informacion()


gerente1 = Gerente("Carlos", 8000, "TI", [empleado1])
gerente1.trabajar()


desarrollador1 = Desarrollador("Luis", 6000, "TI", "Python")
desarrollador1.trabajar()


triangulo1 = Triangulo(10, 5)
triangulo1.calcular_area()


cuadrado1 = Cuadrado(4)
cuadrado1.calcular_area()


lavadora1 = Lavadora("LG", "TurboWash", "A++", 8)
lavadora1.encender()


refrigerador1 = Refrigerador("Samsung", "FrostFree", "A+", True)
refrigerador1.encender()


usuario1 = Usuario("admin", "1234")
usuario1.iniciar_sesion("admin", "1234")


cliente1 = Cliente("pedro99", "abcd")
cliente1.realizar_compra()


