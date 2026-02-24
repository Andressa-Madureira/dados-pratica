#1. Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.

nome = input('Qual é o seu nome?: ')
print(f'Olá, {nome}!')

#2.Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
idade = int(input('Qual é a sua idade?: ')) 
print(f'Olá, {nome}, você tem {idade} anos.')

#3.Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”

altura = float(input('Qual é a sua altura?: '))
print(f'Olá, {nome}, você tem {idade} anos e mede {altura} metros!')

#Calculadora com operadores

#1)Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores. 

primeiro_numero = int(input("Por favor, digite o primeiro número: "))
segundo_numero = int(input("Por favor, digite o segundo número: "))
resultado_soma = primeiro_numero + segundo_numero
print(f'A soma dos números é {resultado_soma}')


#Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
primeiro_numero = int(input("Por favor, digite o primeiro número: "))
segundo_numero = int(input("Por favor, digite o segundo número: "))
terceiro_numero = int(input("Por favor, digite o terceiro número: "))
resultado_soma_tres = primeiro_numero + segundo_numero + terceiro_numero
print(f'A soma dos três números é: {resultado_soma_tres}')

#3)Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
primeiro_numero = int(input("Por favor, digite o primeiro número para a subtração: "))
segundo_numero = int(input("Por favor, digite o segundo número para a subtração: "))
resultado_sub = primeiro_numero - segundo_numero
print(f'O resultado da subtração é: {resultado_sub}')

#4)Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
primeiro_numero = int(input("Por favor, digite o primeiro número para a multiplicação: "))
segundo_numero = int(input("Por favor, digite o segundo número para a multiplicação: "))
resultado_multi = primeiro_numero * segundo_numero
print(f'O resultado da multiplicação é: {resultado_multi}')

#5)Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
def divisao_valor():
    while True:
        try:
            numerador = int(input("Por favor, digite o numerador: "))
            denominador = int(input("Por favor, digite o denominador. Atenção: não pode ser o 0: "))
            resultado_divisao = numerador / denominador
            print(f'O valor da divisão é: {resultado_divisao}')
            break

        except ZeroDivisionError:
            print('Atenção o denominador não pode ser 0. Tente novamente')
        except ValueError:
             print('Por favor, você precisa digitar um número inteiro! Tente novamente, por favor.')
if __name__ == "__main__":
        divisao_valor()

#6)Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
def potencia():
     while True:
          
          try:
               operador = int(input('Por favor, digite o operador: '))
               potencia = int(input('Por favor, digite uma potência'))
               resultado_potencia = operador ** potencia
               print(f'O resultado da potência é: {resultado_potencia}')
               break
          
          except ValueError:
               print('Por favor, digite um número! Informe os valores corretamente')

if __name__ == "__main__":
     potencia()

#7)Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

def calcular_divisao_inteira():
     while True:
          try:
               numerador = int(input("Por favor, digite o numerador: "))
               denominador = int(input("Por favor, digite o denominador. Atenção! O denominador não pode ser o 0."))
               resultado_div_int = numerador//denominador
               print(f"O resultado da divisão inteira é: {resultado_div_int}")
               break

          except ValueError:
               print("Atenção! Valor inválido! Tente novamente, por favor")
          except ZeroDivisionError:
               print("Atenção! O denominador não pode ser o 0. Tente novamente, por favor")
if __name__ == "__main__":
     calcular_divisao_inteira()


#8)Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

def resto_divisao():
     while True:
          try:
               numerador = int(input("Por favor, digite o numerador: "))
               denominador = int(input("Por favor, digite o denominador. ATENÇÃO: Não pode ser o 0: "))
               resultado_resto_divisao = numerador % denominador
               print(f'O resultado do resto da divisão é {resultado_resto_divisao} ')
               break
          except ValueError:
               print("Valor inválido! Por favor, digite um valor válido. ")
          except ZeroDivisionError:
               print("O denominador não pode ser 0. Tente novamente")
if __name__ == "__main__":
     resto_divisao()

#9)Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

def media_notas():
     while True:
          try:
               primeira_nota = float(input("Por favor, digite a primeira nota: "))
               segunda_nota = float(input("Por favor, digite a segunda nota: "))
               terceira_nota = float(input("Por favor, digite a terceira nota: "))
               resultado_media = (primeira_nota + segunda_nota + terceira_nota) / 3
               print(f"A média das 3 notas é : {resultado_media: .2f}")
               break
          except ValueError:
               print("Valor inválido! Por favor, tente novamente!")
if __name__ == "__main__":
     media_notas()

#10) Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.

numeros = [5,12,20,15]
pesos = [1,2,3,4]

soma_numeros = sum(n * p for n, p in zip(numeros, pesos))
resultado_pesos = sum(pesos)
resultado_media_ponderada = soma_numeros/resultado_pesos
print(f'A média ponderada é: {resultado_media_ponderada: .2f}')

#Editando texto

#1)Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.

frase = "Olá, mundo!"
print(frase)   

#2)Crie um código que solicite uma frase e depois imprima a frase na tela
frase = input("Por favor, digite uma frase:")
print(frase)

#3)Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
frase = input("Por favor, digite uma frase:")
print(frase.upper())

#4)Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
frase = input("Por favor, digite uma frase:")
print(frase.lower())
#5)Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.

frase = "   Olá, mundo!   "
print(frase.strip())

#6)Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
frase = input("Por favor, digite uma frase:")
print(frase.strip())

#7)Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase = input("Por favor, digite uma frase:")
print(frase.strip().lower())


#8)Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
frase = input("Por favor, digite uma frase:")
print(frase.replace("e","f"))

#9)Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
frase = input("Por favor, digite uma frase:")
print(frase.replace("a","@"))

#10)Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
frase = input("Por favor, digite uma frase:")
print(frase.replace("s","$"))