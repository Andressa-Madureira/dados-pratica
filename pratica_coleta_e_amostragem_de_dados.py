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

