from cartas.defesa import CartaDefesa

class CartaArmadura(CartaDefesa):
    def __init__(self):
        super().__init__()
        self.nome = "Armadura"
        self.descricao = f"Defesa com armadura bloqueando {self.bloqueio} de dano."
