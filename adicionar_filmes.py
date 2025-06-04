
filmes = []
quantidades=int(input('Quantos filmes? '))
contador=1
while contador<=quantidades:
    nome=input(f"Digite o nome dos filmes {contador}: ")   
    contador=contador+1
    filmes.append(nome)

print(filmes)
    
