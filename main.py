# def main():
#     print("Hello from python-poo!")


# if __name__ == "__main__":
#     main()
from guerrero import Guerrero
from saiyajin import Saiyajin, SaiyajinProtocol
from personaje import Personaje
from torneo import Torneo

from exceptions import DragonBallException, ListadoVacioException
# personajes = [goku, vegeta]
# for personaje in personajes:
#     print(personaje)

goku = Saiyajin("Goku", "1.75m", 9001, "Planeta Vegeta", cola=False)
#print(goku.saludar())
vegeta = Saiyajin("Vegeta", "1.65m", 8500, "Planeta Vegeta", cola=True)
#print(vegeta.saludar())
krilin = Guerrero("Krillin", "1.60m", 3000)
#print(krilin.saludar())
bulma = Personaje("Bulma", "1.70m", 10)
#MAS PARTICIPANTES#
chaoz = Guerrero("Chaoz", "1.50m", 2000)
yamcha = Guerrero("Yamcha", "1.80m", 2500)
ten_shin_han = Guerrero("Ten Shin Han", "1.82m", 4000)
piccolo = Guerrero("Piccolo", "2.00m", 7000)
yajirobe = Guerrero("Yajirobe", "1.75m", 1500)

guerreros: list[SaiyajinProtocol] = [goku, vegeta] #krilin
for guerrero in guerreros:
    print(guerrero.saludar())

#print(goku.atacar())
# print(vegeta.atacar())
# print(krilin.atacar())
#print(goku.transformar_super_saiyajin())
#print(krilin.transformar_super_saiyajin())  # This will raise an AttributeError

torneo_dragon_ball = Torneo("Torneo de Dragon Ball 1")
torneo_dragon_ball.participantes = [goku, vegeta, krilin, bulma, chaoz, yamcha, ten_shin_han, piccolo, yajirobe]
print("=====================================")
print(torneo_dragon_ball.titulo)
print("Lista de participantes (solo peleadores con nivel de fuerza > 1000):")
lista_participantes = torneo_dragon_ball.listar_participantes()
print(lista_participantes)
print("=====================================")
print("Sorteando participantes...")
try:
    torneo_dragon_ball.sortear_participantes([])
except DragonBallException as e:
    print(f"Error: {e}")