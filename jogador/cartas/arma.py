from cartas.ataque import CartaAtaque

class CartaArma(CartaAtaque):
    def __init__(self):
        super().__init__()
        self.nome = "machado"
        self.descricao = f"Golpe com machado causando {self.dano} de dano."
