from typing import Protocol
from personaje import Personaje

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


