class Carro:
    
    def __init__(self, motor, direcao, eletrico):
        self.motor = motor
        self.direcao = direcao
        self.eletrico = eletrico

    def partida(self):
        print('Dando partida no carro...')

    def acelera(self):
        print('Carro acelerado e em movimento')

    def parar(self):
        print('Carro parado')