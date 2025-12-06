#1. 1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

def exibir_numero_maior():
    print('Vamos descobrir qual é o maior número?')
    while True:
        try:
            primeiro_numero = int(input('Digite o primeiro número: '))
            segundo_numero = int(input('Digite o segundo número: '))
            if primeiro_numero > segundo_numero:
                print(f'O {primeiro_numero} é maior')
            elif segundo_numero > primeiro_numero:
                print(f'O {segundo_numero} é maior')
            else:
                print('Os dois números são iguais')
            break
        except ValueError:
            print('Valor inválido! Por favor, digite um número inteiro.')
if __name__ == "__main__":
    exibir_numero_maior()

#2.Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

def percentual_empresa():
    while True:
        try:
            informe_percentual = float(input('Por favor, informe o percentual da empresa: '))
            if informe_percentual > 0:
                print(f'Houve um crescimento de {informe_percentual}%.')
            elif informe_percentual == 0:
                print('Não houve crescimento.')
            else:
                print(f'Houve um descréscimo de {informe_percentual}%.')
            break
        except ValueError:
            print('Valor inválido! Por favor, digite um número real')
if __name__ == "__main__":
    percentual_empresa()

