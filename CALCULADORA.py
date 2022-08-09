# Calculadora_Basica1

operação = input('''
Selecione uma das opções a seguir para começar: :
+ for adição
- for subtração
* for multiplicação
/ for divisão
''')

numero1 = int(input('Insira o primeiro numero: '))
numero2 = int(input('insira o segundo numero: '))

if operação == '+':
    print('{} + {} = '.format(numero1, numero2))
    print(numero1 + numero2)

elif operação == '-':
    print('{} - {} = '.format(numero1, numero2))
    print(numero1 - numero2)

elif operação == '*':
    print('{} * {} = '.format(numero1, numero2))
    print(numero1 * numero2)

elif operação == '/':
    print('{} / {} = '.format(numero1, numero2))
    print(numero1 / numero2)

else:
    print('Selecione uma opção valida!: ')
    