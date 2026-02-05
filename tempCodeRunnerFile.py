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