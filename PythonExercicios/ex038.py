num1 = int(input('Digite o primeiro: '))
num2 = int(input('Digite o outro: '))
if num1 > num2:
    print(f"O {num1} é maior.")
elif num2 > num1:
    print(f'O {num2} é maior.')
else:
    print('Os dois são iguais.')