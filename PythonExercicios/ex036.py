valorcasa = float(input('Qual é o valor da casa?\nR$'))
salario = float(input('Qual é o salário?\nR$'))
anos = int(input('Quantos anos a parcela?\nR: '))
meses = salario * (anos * 12)
minimo = salario * 30 / 100
print(f'Preço casa: R${valorcasa:.2f} em {anos}, é R${meses:.2f}.')
if meses <= minimo:
    print('Empréstimo poder ser concedido.')
else:
    print('Empréstimo negado.')