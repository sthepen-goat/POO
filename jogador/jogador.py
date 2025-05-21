from cartas.comprar import comprar_carta

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.mao = [comprar_carta() for _ in range(7)]

    def esta_vivo(self):
        return self.vida > 0

    def comprar_carta(self):
        if len(self.mao) < 7:
            self.mao.append(comprar_carta())

    def usar_carta(self, indice, oponente):
        carta = self.mao.pop(indice)
        carta.aplicar_efeito(self, oponente)
        self.comprar_carta()
