from typing import Protocol
from main import Personaje
from guerrero import Guerrero

class GuerreroProtocol(Protocol):
    def atacar(self) -> str:
        ...
    def saludar(self) -> str:
        ...

class SaiyajinProtocol(Protocol):
    def transformar_super_saiyajin(self) -> str:
        ...
    def tranformar_ozaru(self) -> str:
        ...
    def saludar(self) -> str:
        ...
    def atacar(self) -> str:
        ...

class Saiyajin(Personaje):
    def __init__(self, nombre, talla, nivel_fuerza, planeta_origen, cola=False):
        super().__init__(nombre, talla, nivel_fuerza)
        self.planeta_origen = planeta_origen
        self.cola = cola
        #self.nivel_fuerza = nivel_fuerza

    def transformar_super_saiyajin(self):
        return f"{self.nombre} se ha transformado en Super Saiyajin!"
    
    def tranformar_ozaru(self):
        return f"{self.nombre} se ha transformado en Oozaru!"
    
    def saludar(self):
        return f"Hola, soy {self.nombre}, soy un Saiyajin y mi poder de pelea es: {self.get_nivel_fuerza()}."
    
    def atacar(self):
        return f"{self.nombre} (saiyajin) está atacando con un poder de {self.get_nivel_fuerza()}!"


goku = Saiyajin("Goku", "1.75m", 9001, "Planeta Vegeta", cola=False)
#print(goku.saludar())
vegeta = Saiyajin("Vegeta", "1.65m", 8500, "Planeta Vegeta", cola=True)
#print(vegeta.saludar())
krilin = Guerrero("Krillin", "1.60m", 3000)
#print(krilin.saludar())

guerreros: list[SaiyajinProtocol] = [goku, vegeta] #krilin
for guerrero in guerreros:
    print(guerrero.saludar())

#print(goku.atacar())
# print(vegeta.atacar())
# print(krilin.atacar())
#print(goku.transformar_super_saiyajin())
#print(krilin.transformar_super_saiyajin())  # This will raise an AttributeError