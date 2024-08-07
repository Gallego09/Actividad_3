import math
class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

if __name__ == "__main__":
    vehiculo = Vehiculo(180, 15000)
    print(vehiculo.velocidad_maxima, vehiculo.kilometraje)




class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")
    
    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
    
    def calcular_distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
    
if __name__ == "__main__":
    punto1 = Punto(0, 0)
    punto2 = Punto(3, 4)
    punto1.mostrar()
    punto1.mover(1, 1)
    punto1.mostrar()
    print(punto1.calcular_distancia(punto2))





class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2
    
    def calcular_perimetro(self):
        return 2 * (abs(self.punto1.x - self.punto2.x) + abs(self.punto1.y - self.punto2.y))
    
    def calcular_area(self):
        return abs(self.punto1.x - self.punto2.x) * abs(self.punto1.y - self.punto2.y)
    
    def es_cuadrado(self):
        return abs(self.punto1.x - self.punto2.x) == abs(self.punto1.y - self.punto2.y)
    
if __name__ == "__main__":
    rectangulo = Rectangulo(punto1, punto2)
    print(rectangulo.calcular_perimetro())
    print(rectangulo.calcular_area())
    print(rectangulo.es_cuadrado())
    







class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def pertenece_al_circulo(self, punto):
        return self.centro.calcular_distancia(punto) <= self.radio

if __name__ == "__main__":
    circulo = Circulo(Punto(0, 0), 5)
    print(circulo.calcular_area())
    print(circulo.calcular_perimetro())
    print(circulo.pertenece_al_circulo(Punto(3, 4)))






class Carta:
    CORAZONES = "Corazones"
    DIAMANTES = "Diamantes"
    TREBOLES = "Tréboles"
    PICAS = "Picas"
    
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

if __name__ == "__main__":
    carta = Carta(10, Carta.CORAZONES)
    print(carta.valor, carta.pinta)







class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar(self, monto):
        self.balance += monto
    
    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
        else:
            print("Fondos insuficientes")
    
    def aplicar_cuota_manejo(self):
        self.balance -= self.balance * 0.02
    
    def mostrar_detalles(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance}")

if __name__ == "__main__":
    cuenta = CuentaBancaria("1234567890", ["Juan Perez"], 1000)
    cuenta.depositar(500)
    cuenta.retirar(200)
    cuenta.aplicar_cuota_manejo()
    cuenta.mostrar_detalles()


