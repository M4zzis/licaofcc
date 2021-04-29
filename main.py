linha = []
numero = int(input("Insira um numero positivo : "))

if(numero < 0):
  print("Numero Invalido")

variavel = 0
contagem = 0
while(numero - numero + variavel < numero):
  resultado = numero - numero + variavel 
  resultado = numero - numero + variavel
  linha.insert(contagem, resultado)
  variavel = variavel + 1
  contagem = contagem + 1

contagem = contagem -1
print(*linha, sep=' ')

while(contagem != 0):

  linha.pop(contagem)
  print(*linha, sep=' ')
  contagem = contagem -1

