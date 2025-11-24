'''
Situação:
    Recebemos uma variável com o nome de uma professora da escola para inserirmos no cadastro. No entanto, precisamos tratar esse texto antes de inserirmos no sistema
    * Objetivo final: ANDRESSA DE OLIVEIRA MADUREIRA
'''

texto = '   Andressa De oliveira madureia '

#Converte strings para maiuscula: str.upper()

#Converte strings para minuscula: str.lower()

print(texto.upper())

#Remove todos os espaços em branco do início e fim de uma string: str.strip()
print(texto.strip())

#Substitui todas as ocorrências do texto 'antigo' na string por 'novo': str.replace(antigo, novo)

print(texto.replace('madureia', 'madureira'))

#Agora é necessário salvar e executar as transformações que atribuímos às saídas fazendo uma acumulação dos métodos

texto = texto.strip().replace('madureia','madureira').upper()

print(texto)
