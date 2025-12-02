#1. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
frase = "Olá, mundo!"
print(frase)

#2.Crie um código que solicite uma frase e depois imprima a frase na tela.
frase = input('Olá, digite uma frase: ')
print(frase)

#3.Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
frase = input('Olá, digite sua frase: ')
transform = frase.upper()
print(transform)

#4. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
frase = input('Olá, digite sua frase: ')
print(frase.lower())

#5.Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
frase = " Olá, meu nome é Andressa  "
print(frase.strip())

#6. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
frase = input('Por favor, digite uma frase: ')
print(frase.strip())

#7. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase = input('Por favor, digite uma frase: ') 
print(frase.strip().lower())

#8. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
frase = input('Por favor, digite uma frase: ') 
print(frase.replace('e','f').replace('E', 'f'))

#9. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
frase = input('Por favor, digite uma frase: ') 
print(frase.replace('a','@').replace('A', '@'))

#10. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
frase = input('Por favor, digite uma frase: ') 
print(frase.replace('s','$').replace('S', '$'))
