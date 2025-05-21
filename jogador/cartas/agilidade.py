from cartas.ataque import CartaAtaque

class CartaAgilidade(CartaAtaque):
    def __init__(self):
        super().__init__()
        self.nome = "Agilidade"
        self.descricao = f"Ataque ágil causando {self.dano} de dano."
