'''
Precisamos trabalhar com os dados abaixo fornecendo:
    * A quantidade total de empregados;
    * A diferença entre o salário mais baixo e mais alto; e
    * A média ponderada da faixa salarial da escola
'''

q_seguranca = 5
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500

total_empregados = q_seguranca + q_docente + q_diretoria
print(total_empregados)

diferenca_salario = s_diretoria - s_seguranca
print(diferenca_salario)

media_salarial = (q_seguranca * s_seguranca + q_docente * s_docente + q_diretoria * s_diretoria) / total_empregados

print(media_salarial)