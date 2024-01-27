nota1 = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 50.0:
    print(f'Com as notas sendo {nota1:.1f} e {nota2:.1f}. Você foi reprovado! Média: {media}')
elif 50.0 <= media <= 69.0:
    print(f'Com as notas sendo {nota1:.1f} e {nota2:.1f}. Você está de RECUPERAÇÃO!\nSua média: {media}.')
elif media >= 70.0:
    print(f'Parabéns!! Você foi APROVADO com uma média de {media:.1f}!')