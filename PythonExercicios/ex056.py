media = 0
idades = []
nomes = []
sexos = []
mulheres20 = []
homemMaisVelho = ''
idadeMaisVelho = 0

for p in range(4):  # Começando em 0 e indo até 3
    nomes.append(str(input(f'Nome da {p + 1}ª pessoa: ')).upper())
    idades.append(int(input(f'Idade da {p + 1}ª pessoa: ')))
    sexos.append(int(input(f'Sexo da {p + 1}ª pessoa (1-Male 2-Female): ')))

    media += idades[p]

    if sexos[p] == 2 and idades[p] < 20:
        mulheres20.append(nomes[p])

    if sexos[p] == 1 and idades[p] > idadeMaisVelho:
        idadeMaisVelho = idades[p]
        homemMaisVelho = nomes[p]

media /= 4

print(f'A média das idades é de {media:.1f}.')
print(f'O nome do homem mais velho é {homemMaisVelho}.')

if not mulheres20:
    print('Não há mulheres com menos de 20 anos.')
else:
    print(f'{len(mulheres20)} mulher(es) têm menos de 20 anos.')

"""Exercício 56:
  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
media = 0
idades = []
nomes = []
sexos = []
mulheres20 = []
velho = []
homemMaisVelho = []
p = 1
menor = idades
for p in range(1, 5):
    nomes.append(str(input(f'Nome da {p}ª pessoa: ')).upper())
    idades.append(int(input(f'Idade da {p}ª pessoa: ')))
    homemMaisVelho = nomes[0]
    media = sum(idades) / 4
    velho = idades[0]
    #
    if p > 1:
        if velho > idades[1] and velho > idades[2] and velho > idades[3]:
            velho = idades[0]
            homemMaisVelho = nomes[0]
        if idades[1] > velho and idades[1] > idades[2] and idades[1] > idades[3]:
            velho = idades[1]
            homemMaisVelho = nomes[1]
        if idades[2] > velho and idades[2] > idades[1] and idades[2] > idades[3]:
            velho = idades[2]
            homemMaisVelho = nomes[2]
        if idades[3] > velho and idades[3] > idades[1] and idades[3] > idades[2]:
            velho = idades[3]
            homemMaisVelho = nomes[3]
    #
    sexos.append(int(input(f'Sexo da {p}ª pessoa (1-Male 2-Female): ')))
    if sexos == 2 and idades[p-1] < 20:
        mulheres20 = nomes[p-1]
    else:
        mulheres20 = 'Não há nenhuma mulher.'
print(f'A média das idades é de {media:.1f}.')
print(f'O nome do homem mais velho é {homemMaisVelho}.')
if len(mulheres20) == 0:
    print('Não há mulheres com menos de 20 anos.')
else:
    print(f'{len(mulheres20)} mulheres têm menos de 20 anos.')
"""