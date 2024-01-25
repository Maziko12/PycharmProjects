print('Homens = (13,75 x peso em quilos) + (5 x altura em centímetros) - (6,76 x idade em anos) + 66,5.')
calculo = int(input('Qual seu peso em quilos?\nR: '))
calculo1 = float(input('Qual é a sua altura em centímetros?\nR: '))
calculo2 = int(input('Qual é a sua idade?\nR: '))
conclusao = (13.75 * calculo) + (5 * calculo1) - (6.76 * calculo2) + 66.5
print(f'Você precisa de {conclusao:.0f} calorias por dia, para manter seu peso.')
