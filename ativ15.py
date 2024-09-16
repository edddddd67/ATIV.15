# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
n1 = float(input("digite primeiro numero"))
n2 = float(input("digite segundo numero"))

op = input('digite a operação que deseja usar: soma, subtração, multiplicação, divisão')

if op == 'soma':
    print(n1 + n2)
elif op == 'multiplicação':
    print( n1 * n2)
elif op =="subtração":
    print (n1 - n2)
if op == "divisão":
    print(n1/n2)
    