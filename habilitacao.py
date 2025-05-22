nome=input('Qual seu nome?')
idade=int(input('qual a sua idade?'))
if idade >= 18:
    print('Maior de idade')
    
    opcao=int (input("Possui carteira de motorista? (sim-1 / nao-2)"))
  
    if opcao==1:
    
     print("Pode dirigir")

    else:
       print('Nao pode dirigir')


else:
    print('Menor de idade')
   
