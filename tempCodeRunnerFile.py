letra = input('Por favor, digite uma letra do alfabeto: ')
            if (letra == 'a' or letra == 'e') or (letra == 'i' or letra == 'o') or letra == 'u':
                print(f'Você digitou a letra {letra}. É uma vogal')
            else:
                print(f'Você digitou a letra {letra}. É uma letra do alfabeto.')