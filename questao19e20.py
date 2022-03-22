# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

  #  Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
  #  326 = 3 centenas, 2 dezenas e 6 unidades.
  #  12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16.
numero = int(input('Digite um numero inteiro positivo: '))

# Extraindo a unidade
unidade = numero % 10

# Eliminando a unidade de nosso número
numero = (numero - unidade)/10

# Extraindo a dezena
dezena = numero % 10

# Eliminando a dezena do número original, fica a centena
numero = (numero - dezena)/10
centena = numero

# Fazendo ser inteiros
dezena = int(dezena)
centena = int(centena)
print(centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)')




#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

   # A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
  # A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
   # A mensagem "Aprovado com Distinção", se a média for igual a 10. 
n1 = int(input('Digite sua 1ª nota: '))
n2 = int(input('Digite sua 2ª nota: '))
n3 = int(input('Digite sua 3ª nota: '))

nota = (n1 + n2 + n3) / 2

if nota >= 7 and nota < 10:     
    print ('Você foi aprovado. Parabéns! ') 
elif nota >= 10:
    print ('Você foi aprovado com distinção :) ')
else:
    print ('Infelizmente você foi reprovado :( ')
    
