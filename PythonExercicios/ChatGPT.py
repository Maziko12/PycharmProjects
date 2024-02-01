media = 0
idades = []
nomes = []
sexos = []
mulheres20 = []
velho = 0
homemMaisVelho = ''
for p in range(1, 5):
    nomes.append(str(input(f'Nome da {p}ª pessoa: ')).upper())
    idades.append(int(input(f'Idade da {p}ª pessoa: ')))
    sexos.append(int(input(f'Sexo da {p}ª pessoa (1-Male 2-Female): ')))
    media += idades[p - 1]
    if sexos[p - 1] == 2 and idades[p - 1] < 20:
        mulheres20.append(nomes[p - 1])
    if sexos[p - 1] == 1 and idades[p - 1] > velho:
        velho = idades[p - 1]
        homemMaisVelho = nomes[p - 1]
media /= 4
print(f'A média das idades é de {media:.1f}.')
print(f'O nome do homem mais velho é {homemMaisVelho}.')
if len(mulheres20) == 0:
    print('Não há mulheres com menos de 20 anos.')
else:
    print(f'{len(mulheres20)} mulheres têm menos de 20 anos.')
