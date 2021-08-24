class Propriedade:
    def __init__(self, nome:str, valor:int):
        self.nome = nome
        self.valor = valor
        self.aluguel = round(self.valor * 0.5)
        self.proprietario = None
    
    def pagar_aluguel(self,jogador:object):
        if self.proprietario != jogador:
            jogador.saldo -= self.aluguel
            if jogador.saldo >= self.aluguel:
                self.proprietario.saldo += self.aluguel
            else:
                self.proprietario.saldo += jogador.saldo
                    
    def comprar(self,jogador:object):
        if jogador.saldo > self.valor:
            jogador.saldo -= self.valor
            self.proprietario = jogador
            