

#Criando um simulador de dado
#Simular o uso de um dado, gerando um valor aleatório de 1 a 6
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado digite "s" ou "n"? '

    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim' or resposta == 's':
            self.GerarValorDoDado()
            self.ContinuaJogar()
        elif resposta == 'não' or resposta == 'n':
            print('Agradecemos sua participação!')
            quit()
        else:
            print('Favor digitar sim ou não')

    def GerarValorDoDado(self):
        self.cont = 1
        while self.cont < 6:
            self.palpite = int(input('Digite um palpite entre 1 e 6: '))
            self.num = (random.randint(self.valor_minimo, self.valor_maximo))
            print(f"Numero sorteado: {self.num}")
            self.Palpite()
            self.cont += 1

    def Palpite(self):
        if self.palpite == self.num:
            print(f'PARABÉNS VOCÊ ACERTOU APÓS {self.cont} TENTATIVAS')
            quit()
        else:
            print('INFELIZMENTE VOCÊ ERROU ')

    def ContinuaJogar(self):
        opcao = int(input('Digite "1" para continuar e "0" para encerrar '))
        while opcao:
            if opcao == 1:
                self.Iniciar()
            elif opcao == 0:
                print("Fim...")
                opcao = False

simulador = SimuladorDeDado()
simulador.Iniciar()