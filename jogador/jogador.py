from cartas.comprar import comprar_carta

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 10
        self.mao = [comprar_carta() for _ in range(7)]  

    def comprar(self):
        if len(self.mao) < 7:
            self.mao.append(comprar_carta())
