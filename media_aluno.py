print("-------SISTEMA DE PROVAS---------")
nome=input('Qual o nome do aluno?')
serie=input("Qual turma?")
provas=int(input('Quantas Provas o aluno fez? '))
a=1
soma=0
while a<=provas:
    notas=float(input(f'Nota da prova {a}: '))
    a= a+1
    soma=soma+notas


media=(soma/provas)
print(f'A média do(a) aluno(a) {nome} da turma {serie} será:{media:.2f}')


if media<=5:
    print('OBS:Precisa estudar mais,sei que consegue.')

elif media<=8.9:
    print("OBS:Está preste a melhorar,continue focado!")

else:
    print('OBS:Parabéns, seu esforço valeu a pena.')
    