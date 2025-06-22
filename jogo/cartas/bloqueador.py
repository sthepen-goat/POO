from cartas.defesa import CartaDefesa
import random
class CartaBloqueador(CartaDefesa):
    def __init__(self):
        super().__init__()
        defensor = random.randint(1, 3)
        if defensor ==  1:
            self.nome = "Bloqueio feroz"
            self.descrição = f"Bloqueia {self.bloqueio} de dano."
        if defensor == 2:
            self.nome = "Bloqueio veloz"
            self.descrição = f"Bloqueia com velocidade {self.bloqueio}"
        if defensor == 3:
            self.nome = "Bloqueio de ferrro"
            self.descrição = f"Bloqueia com o ferro {self.bloqueio}"
    
