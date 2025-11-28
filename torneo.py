class Torneo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.participantes = []

    
    def listar_participantes(self):
        return [participante.nombre for participante in self.participantes if participante.get_nivel_fuerza() > 1000]