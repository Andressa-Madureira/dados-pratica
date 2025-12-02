#10. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
frase = input('Por favor, digite uma frase: ') 
print(frase.replace('s','$').replace('S', '$'))