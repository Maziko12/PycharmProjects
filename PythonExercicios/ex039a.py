pergunta = int(input('Você já se alistou?(1-Sim/2-Não) '))
idade = int(input('Qual sua idade? '))
ano = int(input('Em que ano nasceu? '))
msg = {"***********************************"
       "**************QUE LEGAL************"
       "***********Meus parabéns!**********"
       "***********************************"
       "Fim!"}
if 2024 - ano < 18:
    print(f'Você vai se alistar em breve, daqui {18 - idade} anos.')
elif 2024 - ano == 18:
    if pergunta == 1:
        print(f'Uau, wow, fique com essa mensagem então!\n{msg}')
    else:
        print('Você precisa se alistar.')
elif 2024 - ano > 18:
    if pergunta == 1:
        print(f'Uau, wow, fique com essa mensagem então!\n{msg}')
    else:
        print(f'Já passou do tempo e já se foram {idade-18} anos.')
