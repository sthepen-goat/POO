import random
from cartas import Carta

class CartaDefesa(Carta):
    def __init__(self):
        bloqueio = random.randint(1, 3)
        super().__init__("Carta de Defesa", f"Bloqueia {bloqueio} de dano.")
        self.bloqueio = bloqueio
        self.precisa_alvo = False


    def aplicar_efeito(self, jogador, oponente):
        jogador.vida += self.bloqueio
        print(f"{jogador.nome} usa {self.nome} e recupera {self.bloqueio} de vida.")