from cartas.ataque import CartaAtaque
import random
class CartaArma(CartaAtaque):
    def __init__(self):
        super().__init__()
        escolha = random.randint(1, 3)
        if escolha == 1:
            self.nome = "Espada Furiosa"
            self.descrição = f"Golpe furioso {self.dano}"
        if escolha == 2:
            self.nome = "Machado Cortante"
            self.descrição = f"Corte afiado {self.dano}"
        if escolha == 3:
            self.nome = "Lança Veloz"
            self.descrição = f"Furacão veloz {self.dano}"
