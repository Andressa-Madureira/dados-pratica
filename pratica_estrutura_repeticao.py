#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
primeiro_numero = int(input("Por favor, digite o primeiro numero inteiro: "))
segundo_numero = int(input("Por favor, digite o segundo numero inteiro: "))
inicio = min(primeiro_numero, segundo_numero)
fim = max(primeiro_numero, segundo_numero)
for numero in range(inicio + 1, fim):
    print(numero)

#2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

a = 4 
b = 10
contador = 0
while a < b:
    a *= 1.03
    b *= 1.015
    contador += 1
print(f"Serão necessários {contador} dias  para que a   A ultrapasse a  B.")


for avaliacao in range(1,16):
    while True:
        try:
            nota = float(input(f"Digite a {avaliacao}° nota entre 0 e 5:"))
            if nota < 0 or nota > 5:
                print("Nota inválida! Por favor, digite uma nota entre 0 e 5.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")

    