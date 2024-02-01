maior = []
menor = []
for ano in range(0, 7):
    nasc = int(input('Digite seu ano de nascimento: '))
    if 2024 - int(nasc) >= 21:
        maior.append(nasc)
    elif 2024 - nasc < 21:
        menor.append(nasc)
    else:
        print('Entrada errada!')
print(f'Pessoas de menor: {menor}.')
print(f'Pessoas de maior: {maior}')