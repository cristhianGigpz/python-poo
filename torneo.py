import random
from exceptions import ListadoVacioException, ListadoNoEsListaException

class Torneo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.participantes = []

    
    def listar_participantes(self):
        return [participante.nombre for participante in self.participantes if participante.get_nivel_fuerza() > 1000]
    

    def sortear_participantes(self, lista_filtrada: list = []):
        if not isinstance(lista_filtrada, list):
            raise ListadoNoEsListaException("El argumento proporcionado no es una lista.")
        if not lista_filtrada:
            raise ListadoVacioException("El listado de participantes está vacío.")
        random.shuffle(lista_filtrada)
        for index, participante in enumerate(lista_filtrada, start=1):
            print(f"{index} - {participante}")
        
        


        