# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
op = input('Feminino (F) e Masculino (M)')
op = op.upper()
if(op == 'F'):
  print('F - Feminino!')
elif(op == 'M'):
  print('M - Masculino!')
else:
  print('Sexo Inválido!')
