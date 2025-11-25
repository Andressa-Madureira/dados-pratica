#1. Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.

nome = input('Qual é o seu nome?: ')
print(f'Olá, {nome}!')

#2.Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
idade = int(input('Qual é a sua idade?: ')) 
print(f'Olá, {nome}, você tem {idade} anos.')

#3.Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”

altura = float(input('Qual é a sua altura?: '))
print(f'Olá, {nome}, você tem {idade} anos e mede {altura} metros!')