
from abc import ABC, abstractmethod

class Carta(ABC):
    def __init__(self, nome: str, descricao):
        self.nome = nome
        self.descricao = descricao

    @abstractmethod
    def aplicar_efeito(self, jogador, oponente):
        pass
