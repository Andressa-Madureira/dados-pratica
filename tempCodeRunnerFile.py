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