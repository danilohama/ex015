# escreva um programa que pergunte a qtd de km percorrido por um carro alugado e a qtd de dias q foi alugado
# calcule o preço a pagar  sabendo que o carro custa R$ 60 por dia e R$0,15 por km rodado

dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))

pagar = (dia * 60) + (km * 0.15)

print('Valor a pagar por dia é {:.2f}'.format(pagar))
