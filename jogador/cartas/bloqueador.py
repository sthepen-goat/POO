from cartas.defesa import CartaDefesa

class CartaBloqueador(CartaDefesa):
    def __init__(self):
        super().__init__()
        self.nome = "Bloqueador"
        self.descricao = f"Defesa com Bloqueador impedindo {self.bloqueio} de dano."
