# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

 #   Dicas:
 #  Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
 #  Triângulo Equilátero: três lados iguais;
 #  Triângulo Isósceles: quaisquer dois lados iguais;
 #  Triângulo Escaleno: três lados diferentes; 
  
a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))
# Testando se é triângulo
if (a + b < c) or (a + c < b) or (b + c < a):
  print('Nao é um triangulo')
elif (a == b) and (a == c) :
  print('Equilatero')
elif (a==b) or (a==c) or (b==c):
  print('Isósceles')
else:
  print('Escaleno')
  
  
# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

 #   Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
 #  Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
 #   Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
 #   Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
#formula de baskara
import math
print('Equaçao do 2º grau da forma: ax² + bx + c')
a = int( input('Coeficiente a: ') )
if (a == 0):
    print('Se a = 0, não é equação do segundo grau :) ')
else:
    b = int( input('Coeficiente b: ') )
    c = int( input('Coeficiente c: ') )
    delta = b * b - (4 * a * c)

    if delta < 0:
        print('Delta menor que 0. Raízes imaginárias :)')
    elif delta == 0:
        raiz = -b / (2 * a)
        print('Delta = 0 , raiz = ',raiz)
    else:
        raiz1 = (-b + math.sqrt(delta) ) / (2*a)
        raiz2 = (-b - math.sqrt(delta) ) / (2*a)
        print('Raizes: ', raiz1,' e ', raiz2)
