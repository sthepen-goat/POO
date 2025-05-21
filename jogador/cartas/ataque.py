import random
from cartas import Carta

class CartaAtaque(Carta):
    def __init__(self):
        dano = random.randint(5, 15)  
        super().__init__("Carta de Ataque", f"Causa {dano} de dano ao oponente.")
        self.dano = dano

    def aplicar_efeito(self, jogador, oponente):
        oponente.vida -= self.dano
        print(f"{jogador.nome} usa {self.nome} e causa {self.dano} de dano a {oponente.nome}.")
