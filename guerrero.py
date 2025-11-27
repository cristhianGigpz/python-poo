from main import Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, talla, nivel_fuerza):
        super().__init__(nombre, talla, nivel_fuerza)

    def atacar(self):
        return f"{self.nombre} está atacando con un poder de {self.get_nivel_fuerza()}!"
    
    def saludar(self):
        return f"Hola, soy {self.nombre}, soy un Guerrero y mi poder de pelea es: {self.get_nivel_fuerza()}."

    