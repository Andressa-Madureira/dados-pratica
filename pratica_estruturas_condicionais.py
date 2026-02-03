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

#Não commitei o terceiro 
#3. Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

def verificar_alfabeto():
    while True:
        try:
            entrada = input("Por favor, digite uma única letra do alfabelto(VOGAL ou CONSOANTE): ").strip()
            if len(entrada) != 1:
                raise ValueError("ERRO: Por favor, digite apenas uma letra por vez: ")

            letra = entrada.lower()

            if not letra.isalpha():
                raise ValueError("ERRO: Entrada inválida! Digite apenas letras de A a Z: ")

            if letra in 'aeiou':
                print(f'{letra.upper()} é uma vogal')
            else:
                print(f'{letra.upper()} é uma consoante')
            break

        except ValueError as e:
            print(f'\n{e}\n')
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}\n")

verificar_alfabeto()

#4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

valores_carros = [85000, 65080, 97300]

maximo = max(valores_carros)

minimo = min(valores_carros)

print(f'O valor máximo é {maximo}')
print(f'O valor mínimo é {minimo}')

#5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

lista_valor = []

valor_agua = float(input('Qual é o valor da água?'))
valor_guarana = float(input('Qual é o valor do guaraná?'))
valor_chocolate= float(input('Qual é o valor do chocolate?'))

lista_valor.append(valor_agua)
lista_valor.append(valor_guarana)
lista_valor.append(valor_chocolate)

print(lista_valor)

barato = min(lista_valor)

if barato == valor_agua:
    print(f'O produto mais barato é a água')
elif barato == valor_chocolate:
    print(f'O produto mais barato é o chocolate')
else:
    print(f'O produto mais barato é o guaraná')

#6) Escreva um programa que leia três números e os exiba em ordem decrescente.

ordem_numeros = []

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

ordem_numeros.append(num1)
ordem_numeros.append(num2)
ordem_numeros.append(num3)

print(ordem_numeros)

ordem_numeros.sort()