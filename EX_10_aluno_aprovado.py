# Escreva um código que pede a nota de duas provas do aluno e verifique se o aluno foi aprovado com as condições abaixo:
# O aluno precisa ter média maior que 7 e não pode ter tirado zero em nenhuma nota.
# Não é necessário usar estruturas condicionais, apenas expressões lógicas conforme estudado no material de expressões lógicas.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite a primeira nota: 10
# Digite a segunda nota: 8
# Aluno aprovado? True

# Exemplo 2:

# Digite a primeira nota: 10
# Digite a segunda nota: 0
# Aluno aprovado? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
provas=int(input(' Qual a quantidade de provas feitas: '))
a=1
soma=0



while a<=provas:
    notas=float(input(f' Digite a nota {a}: '))
    a= a+1
    soma=soma+notas

media=(soma/provas)

print(media>=5)