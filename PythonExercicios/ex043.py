peso = float(input('Qual seu peso em quilos?\nR: '))
altura = float(input('Qual é a sua altura em centímetros?\nR: '))
IMC = peso / (altura ** 2)
if IMC <= 18.5:
    print(f'Você está abaixo do peso, seu IMC é {IMC:.2f}.')
elif 18.5 <= IMC <= 25.0:
    print(f'VOCÊ ESTÁ NO PESO IDEAL! IMC: {IMC:.2f}.')
elif 25.0 <= IMC <= 30.0:
    print(f'Você tem Sobrepeso: {IMC} de IMC.')
elif 30.0 <= IMC <= 40.0:
    print(f'Está com obesidade...IMC de {IMC:.2f}!')
elif IMC > 40.0:
    print(f'Seu caso é grave, e está com Obesidade mórbida! IMC {IMC:.2f}.')
print('Zambumcha?')