cardapio={
    'Entradas': ['Batata Frita Curly','Casquinha de pizza','Pasteizinhos assados '],
    'Pratos': ['Explosão de Sabores','Delícia Tropical','Prato da Paz'],
    'Sobremesa': ['Arco-íris de Frutas','Melodia de Morango','Estrela de Framboesa'],
    'Bebidas': ['Limonada Suíça','Raspadinha de morango','piña colada']
}

def mostrar_carpadio():
    for i in range(len(cardapio['Entradas'])):
        print(cardapio['Entradas'][i])
 
    for i in range(len(cardapio['Pratos'])):
          print(cardapio['Pratos'] [i])
    


def menu():
    print('|----Lista do chefe----|')
    print('(1) Mostrar cardapio')
    print('(2) Adicionar prato')
    print('(3) Remover prato')
    print('(4) Sair')
    opcao=int(input('Escolha a opção: '))
    if opcao==1:
        mostrar_carpadio()

    elif opcao==2:
            print('Você escolheu a opção 2')

    elif opcao==3:
            print('Você escolheu a opção 3')

    elif opcao==4:
            print('Sair')

    else:
            print('Está opção não existe')



     

menu()



