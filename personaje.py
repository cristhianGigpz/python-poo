class Personaje:
    def __init__(self, nombre, talla, nivel_fuerza):
        self.nombre = nombre
        self.talla = talla
        self.__nivel_fuerza = nivel_fuerza

    def __str__(self):
        return f"Personaje(nombre={self.nombre}, talla={self.talla}, nivel_fuerza={self.nivel_fuerza})"

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}, y mi nivel de fuerza es: {self.get_nivel_fuerza()}."
    
    def get_nivel_fuerza(self):
        return self.__nivel_fuerza
    
    def set_nivel_fuerza(self, nuevo_nivel):
        if nuevo_nivel >= 0:
            self.__nivel_fuerza = nuevo_nivel
        else:
            print("El nivel de fuerza no puede ser negativo.")