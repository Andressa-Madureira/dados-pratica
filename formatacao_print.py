nome = "Ana Maria"
idade = 17
print(f"O nome da aluna é {nome} e sua idade é {idade} anos.")
'''
Operador de formatação:
    string: %s
    inteiro: %d
    float: %f
    caractere: %c
'''

#string
nome_aluno = 'Fabricio Daniel'
print('Nome do aluno: %s' %(nome_aluno))

nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45


#string - decimal - float: Devemos ordená-las conforme o surgimento no texto e separá-los por virgulas
print('Nome do aluno é %s, ele tem %d anos e sua média é %f.' %(nome_aluno, idade_aluno, media_aluno))

#Trabalhando com float: Podemos determinar a quantidade casas decimais - %2f(2 casas decimais): 8.45
print('Nome do aluno é %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno, idade_aluno, media_aluno))

x = True
print("Valor de x: %s" % str(x))

#É possível também usar o método format - é mais flexível e permite passar as variáveis diretamente dentro da string
nome_aluno = 'Fabricio Daniel'

print('Nome do aluno: {}'.format(nome_aluno))

nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45

print('Nome do aluno é {}, ele tem {} anos e sua média é {}.' .format(nome_aluno, idade_aluno, media_aluno))


#Caracteres especiais:

#\n -> Pular uma linha
texto = print("Estudar é um esforço constante,\nÉ como cultivar uma planta,\nPrecisamos de dedicação e paciência,\nPara ver o fruto amadurecer.")

#\t -> adiciona um espaço de tabulação no texto 
texto_tab = print('Quantidade\tQualidade\n5 amostras\tAlta\n3 amostras\tBaixa')

#\\ -> é usado para imprimir uma única barra invertida
texto_barra_invertida = print("Caminho do arquivo: C:\\arquivos\\documento.csv")

#\" -> é usado para imprimir aspas duplas
texto_aspas_duplas = print("Ouvi uma vez \"Os frutos do conhecimento são os mais doces e duradouros de todos.\"")

#\' -> é usado para imprimir aspas simples 
texto_aspas_simples = print('Minha professora uma vez disse \'Estudar é a chave do sucesso.\' ')