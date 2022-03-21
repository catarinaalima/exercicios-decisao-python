# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

p1 = input("Digite o 1° preço: ")
p2 = input("Digite o 2° preço: ")
p3 = input("Digite o 3° preço: ")

def menor():
    if p1 < p2 and p3 and p1:
        print ('O produto 1 é o mais barato! ')
    elif p2 < p1 and p3:
        print ('O produto 2 é o mais barato! ')
    elif p3 < p1 and p2:
        print ('O produto 3 é o mais barato! ')

    #Se alguns numeros forem iguais

    elif p1 == p2 and p1 and p2 < p3:
        print ('O produto 1 e 2 são os mais baratos! ')
    elif p1 == p3 and p1 and p3 < p2:
        print ('O produto 1 e 3 são os mais baratos! ')
    elif p2 == p3 and p2 and p3 < p1:
        print ('O produto 1 e 2 são os mais baratos! ')

    #Se todo os numero forem iguais

    else:
        print ('Todos os preços são iguais! ')

menor() # chama a função menor!

# Faça um Programa que leia três números e mostre-os em ordem decrescente. 
primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

print(primeiro,'-',segundo,'-',terceiro)

if(terceiro > segundo):
        aux = terceiro
        terceiro = segundo
        segundo = aux

if(segundo > primeiro):
        aux = segundo
        segundo = primeiro
        primeiro = aux

if(terceiro > segundo):
        aux = terceiro
        terceiro = segundo
        segundo = aux

print(primeiro,'-',segundo,'-',terceiro)
