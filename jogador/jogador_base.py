class JogadorBase:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 300
        self.posicao = 0
    
    def saldo_positivo(self):
        if self.saldo > 0:
            return True
        return False
    
    def avancar_posicao(self, valor_dados:int):
        if (self.posicao + valor_dados) in range(0,21):
            self.posicao += valor_dados
            return self.posicao
        self.posicao = (self.posicao-20) + valor_dados
        self.saldo += 100
        return self.posicao
