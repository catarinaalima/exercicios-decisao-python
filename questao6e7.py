# Faça um Programa que leia três números e mostre o maior deles. 
num1 = int(input("Número um: "))
num2 = int(input("Número dois: "))
num3 = int(input("Número três: "))

if num1 > num2 and num1 > num3:
    print("O número um é o maior: ", num1)
elif num2 > num1 and num2 > num3:
    print("O número dois é o maior: ", num2)
elif num3 > num1 and num3 > num2:
    print("O número três é o maior: ", num3)
    
    
# Faça um Programa que leia três números e mostre o maior e o menor deles. 
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
menor = num1
if num2 < num3 and num2 < num1:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3
print(f"O menor número digitado foi: {menor}")
print(f"O maior número digitado foi: {maior}")
