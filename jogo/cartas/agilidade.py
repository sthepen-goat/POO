from cartas.ataque import CartaAtaque
import random

class CartaAgilidade(CartaAtaque):
    def __init__(self):
      super().__init__()
      seletor = random.randint(1, 3)
      if seletor == 1:
         self.nome = "Agilidade Feroz"
         self.descrição = f"Golpe feroz {self.dano}"
      if seletor == 2:
         self.nome = "Agilidade Veloz"
         self.descrição = f"Golpe veloz {self.dano}"
      if seletor == 3:
         self.nome = "Agilidade de Ferro"
         self.descrição = f"Golpe de ferro {self.dano}"