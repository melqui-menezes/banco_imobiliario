from jogador.jogador_base import JogadorBase


class Impulsivo(JogadorBase):
    
    def __init__(self, name):
        return  super().__init__(name)
    
    def decidir_acao(self, propriedade):
        if propriedade.proprietario:
            propriedade.pagar_aluguel(self)
        else:
            propriedade.comprar(self)