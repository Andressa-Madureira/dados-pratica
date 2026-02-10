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