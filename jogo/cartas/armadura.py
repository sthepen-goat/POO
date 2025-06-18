from cartas.defesa import CartaDefesa
import random

class CartaArmadura(CartaDefesa):
    def __init__(self):
        super().__init__()
        escolha = random.randint(1, 3)
        if escolha ==  1:
            self.nome = "Armadura de Couro"
            self.descrição = f"Bloqueia {self.bloqueio} de dano."
        if escolha == 2:
            self.nome = "Armadura de ossos"
            self.descrição = f"Bloqueia com os ossos {self.bloqueio}"
        if escolha == 3:
            self.nome = "Armadura de Ferro"
            self.descrição = f"Bloqueia com o ferro {self.bloqueio}"
        
