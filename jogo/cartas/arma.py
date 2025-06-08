from cartas.ataque import CartaAtaque
import random

class CartaArma(CartaAtaque):
    def __init__(self):
        self.raio = random.randint(0, 2)
        super().__init__()
        
        escolha = random.randint(1, 3)
        if(self.raio == 0):
         if escolha == 1:
            self.nome = "Espada Furiosa"
            self.descricao = f"Golpe furioso {self.dano}"
         elif escolha == 2:
            self.nome = "Machado Cortante"
            self.descricao = f"Corte afiado {self.dano}"
         elif escolha == 3:
            self.nome = "Lança Veloz"
            self.descricao = f"Furacão veloz {self.dano}"
        if(self.raio > 0 ):
           if escolha == 1:
            self.nome = "Espada Furiosa"
            self.descricao = f"Golpe furioso {self.dano} e ganhe {self.raio} turnos"
           elif escolha == 2:
            self.nome = "Machado Cortante"
            self.descricao = f"Corte afiado {self.dano} e ganhe {self.raio} turnos"
           elif escolha == 3:
            self.nome = "Lança Veloz"
            self.descricao = f"Furacão veloz {self.dano} e  ganhe {self.raio} turnos"
            
