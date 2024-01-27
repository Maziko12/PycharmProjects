num = int(input('Digite um número: '))
tipo = input('Qual tipo você quer ele?\nR: ')
if tipo == "binario":
    print(f"Seu número fica {bin(num)} em binário.")
elif tipo == "octadecimal":
    print(f"Seu número fica {oct(num)} em octa.")
elif tipo == "hexadecimal":
    print(f'Seu num fica {hex(num)} em hexa.')
print('Fim!')