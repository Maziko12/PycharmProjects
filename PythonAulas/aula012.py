nome = str(input('Qual é o seu nome?\nR: '))
if nome == 'Guanabara' or nome == 'Leonardo' or nome == 'Leo':
    print('Que nome bonito!')
    if nome == 'Leo':
        nome = 'Leonardo'
    elif nome == 'Leonardo':
        nome = 'Leo'
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
print('Tenho um bom dia {}.'.format(nome))
if nome in 'Leo Leonardo Guanabara Pedro Maria Paulo':
    print('Pelo visto o rei das maldições pode ganhar de você, e no fim acabou, adeus Satoru Gojo...')
print(f'{nome} é o grande vencedor(a)!')