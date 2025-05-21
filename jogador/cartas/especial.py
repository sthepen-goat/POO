import random
from cartas import Carta

class CartaEspecial(Carta):
    def __init__(self):
        self.dano = random.randint(5, 10)
        self.cura = random.randint(3, 8)
        super().__init__("Especial", f"Dano: {self.dano}, Cura: {self.cura}")

    def aplicar_efeito(self, jogador, oponente):
        oponente.vida -= self.dano
        jogador.vida += self.cura
        print(f"{jogador.nome} causa {self.dano} de dano e cura {self.cura}.")
