# 48 - Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
# 12376489
# = > 98467321

numero = input('Digite um Número: ')
print(f'Número Invertido: {numero[:: - 1]}')
