#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.

primeiro_valor = int(input("Por favor, digite o primeiro valor: "))
segundo_valor = int(input("Por favor, digite o segundo valor: "))
resultado_soma = primeiro_valor + segundo_valor
print(f'A soma dos dois valores é: {resultado_soma}')

#2.Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.(os inputs para o 2 valores já estão acima)

primeiro_valor_soma = int(input("Por favor, digite o primeiro valor: "))
segundo_valor_soma = int(input("Por favor, digite o segundo valor: "))
terceiro_valor_soma = int(input("Por favor, digite o terceiro valor: "))
resultado_soma_tres_valores = primeiro_valor_soma + segundo_valor_soma + terceiro_valor_soma
print(f'A soma dos três valores é: {resultado_soma_tres_valores}')

#3. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.

primeiro_valor_n1 = int(input('Por favor, digite o primeiro valor: '))
segundo_valor_n2 = int(input('Por favor, digite o segundo valor: '))
resultado_subtracao = primeiro_valor_n1 - segundo_valor_n2
print(f'O valor da diferença é: {resultado_subtracao}')

#4. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
primeiro_valor_multi = int(input('Por favor, digite o primeiro valor: '))
segundo_valor_multi = int(input('Por favor, digite o segundo valor: '))
resultado_multi = primeiro_valor_multi * segundo_valor_multi
print(f'O resultado da multiplicação é: {resultado_multi}')

#5 - Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
#Resultado com o que aprendi com o tratamento das exceções
def calcular_divisao_segura():
    while True:
        try:
            numerador = int(input('Por favor, digite o numerador: '))
            denominador = int(input('Por favor, digite o denominador.(Não pode ser o 0 e precisa ser um número inteiro: ) '))
            resultado_valor_divisao = numerador / denominador
            print(f'O resultado é {resultado_valor_divisao}')
            break

        except ZeroDivisionError:
            print('Atenção o denominador não pode ser 0. Tente novamente')
        except ValueError:
            print('Atenção. Você precisa digitar um número inteiro. Tente novamente')
if __name__ == "__main__":
    calcular_divisao_segura()
        
#Resultado sem utilizar o tratamento das execeções
numerador = int(input('Por favor, digite o numerador: '))
denominador = int(input('Por favor, digite o denominador.(Não pode ser o 0 e precisa ser um número inteiro: ) '))

while denominador == 0:
    print('Você digitou o 0. ')
    denominador = int(input('Por favor, digite o denominador.(Não pode ser o 0 e precisa ser um número inteiro: ) '))
resultado_valor_divisao = numerador / denominador
print(f'O resultado é {resultado_valor_divisao}')

#6. Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.

def calcular_potencia():
    while True:
        try:
            operador = int(input('Por favor, digite o 1° número: '))
            potencia = int(input('Por favor, digite o 2° número: '))
            resultado_potencia = operador ** potencia
            print(f'O resultado da potência é: {resultado_potencia}')
            break
        except ValueError:
            print('Atenção! Você precisa digitar um número inteiro. Tente novamente.')
if __name__ == "__main__":
    calcular_potencia()

#7. Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

def calcular_divisao_inteira():
    while True:
        try:
            numerador = int(input('Por favor, digite o numerador: '))
            denominador = int(input('Por favor, digite o denominador(NÃO pode ser zero): '))
            resultado_divisao_inteira = numerador // denominador
            print(f'O resultado da divisão inteira é {resultado_divisao_inteira}')
            break
        except ValueError:
            print('Valor inválido. Por favor, digite um número inteiro')
        except ZeroDivisionError:
            print('Atenção! O denominador não pode ser 0. Tente novamente')
if __name__ == "__main__":
    calcular_divisao_inteira()

#8. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

def calcular_resto_divisao():
    while True:
        try:
            numerador = int(input('Por favor, digite o numerador: '))
            denominador = int(input('Por favor, digite o denominador(NÃO pode ser o zero): '))
            resultado_resto_divisao = numerador % denominador 
            print(f'O resultado do resto da divisão é: {resultado_resto_divisao}')
            break
        except ZeroDivisionError:
            print('Atenção! O denominador não pode ser 0. Tente novamente')
        except ValueError:
            print('Valor inválido. Por favor, digite um número inteiro')
if __name__ == "__main__":
    calcular_resto_divisao()

#9. Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

def calcular_media_notas():
    while True:
        try:
            primeira_nota = float(input('Por favor, digite a sua 1° nota: '))
            segunda_nota = float(input('Por favor, digite sua 2° nota: '))
            terceira_nota = float(input('Por favor, digite sua 3° nota: '))
            resultado_media = (primeira_nota + segunda_nota + terceira_nota) / 3
            print(f'A média das notas é: {resultado_media:.2f}')
            break
        except ValueError:
            print('Valor inválido! Por favor, digite um número real.')
if __name__ == "__main__":
    calcular_media_notas()

#10. Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.

import numpy as np

numeros = np.array([5, 12, 20, 15])
pesos = np.array([1, 2, 3, 4])

# O cálculo deve dar (5*1 + 12*2 + 20*3 + 15 * 4) / (1+2+3+4) = 149 / 10 = 14,9
media = np.average(numeros, weights=pesos)

print(f"Resultado da Média Ponderada: {media}")

if __name__ == "__main__":
    pass