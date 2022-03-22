# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 

dia = int(input('Digite um número que corresponde ao dia da semana: '))
if (dia == 1):
  print('Domingo :( ')
elif (dia == 2):
  print('Segunda :( ')
elif (dia == 3):
  print('Terça :/ ')
elif (dia == 4):
  print('Quarta :\ ')
elif (dia == 5):
  print('Quinta :/ ')
elif (dia == 6):
  print('Sexta :) ')
elif (dia == 7):
  print('Sabado :)) ')
else:
  print('Dia Inválido!')

# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 


 #Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0        A
  #Entre 7.5 e 9.0         B
  #Entre 6.0 e 7.5         C
  #Entre 4.0 e 6.0         D
  #Entre 4.0 e zero        E
  
v1 = input('Digite o valor da primeira nota: ')
v2 = input('Digite o valor da segunda nota: ')

nota = (v1 + v2) /2

#nota A

if nota >= 9 and nota <= 10:
    print ('A nota da primeira prova: ',v1)
    print ('A nota da segunda prova: ',v2)
    print ('——————————')
    print ('Você tirou um A!')
    print ('Sua media é de:',nota)
    print ('Você foi aprovado!')

#nota B

elif nota >= 7.5 and nota < 9:
    print ('A nota da primeira prova: ',v1)
    print ('A nota da segunda prova: ',v2)
    print ('——————————')
    print ('Você tirou um B!')
    print ('Sua media é de:', nota)
    print ('você foi aprovado!!')

#nota C

elif nota >= 6.5 and nota < 7.5:
    print ‘A nota da primeira prova: ‘,v1
    print ‘A nota da segunda prova: ‘,v2
    print ‘——————————‘
    print ‘Você tirou um C!’
    print ‘Sua media é de:’,nota
    print ‘você foi aprovado!!’

#nota D

elif nota >= 4 and nota < 6:
    print ‘A nota da primeira prova: ‘,v1
    print ‘A nota da segunda prova: ‘,v2
    print ‘——————————‘
    print ‘Você tirou um D!’
    print ‘Sua media é de:’,nota
    print ‘você foi reprovado!!’

#nota E

elif nota < 4:
    print ‘A nota da primeira prova: ‘,v1
    print ‘A nota da segunda prova: ‘,v2
    print ‘——————————‘
    print ‘Você tirou um E!’
    print ‘Sua media é de:’,nota
    print ‘você foi reprovado!!’
