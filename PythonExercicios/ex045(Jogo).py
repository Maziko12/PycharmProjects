import random
import os
import time

player = int(input('Qual você escolhe?\n'
                   '1-Pedra, 2-Papel, 3-Tesoura\n'
                   'Eu vou jogar: '))
jogo = random.randint(1, 3)
vitoriaCase = ["A vitória é uma necessidade, não uma opção. 🏆",
               "Quanto maiores as dificuldades, mais doce o sabor da vitória. 🥇",
               "A vitória é o prêmio daqueles que não desistem de sonhar.",
               "Coragem para começar e força para perseverar. A vitória virá! 💪",
               "A vitória é destinada àqueles que não medem esforços para lutar.",
               "A vitória pertence aos filhos de Deus. 🙏",
               "Sempre é tempo de recomeçar. Creia e a vitória será sua!",
               "A vitória é a recompensa da perseverança.",
               "A vitória não é daqueles que nunca falharam, mas dos que insistem em lutar.🤩",
               "Grandes vitórias são o resultado de dedicação, esforço e muito trabalho duro. 💪",
               'Mas é isso kkkkkkkkkk, eu consegui ganhar velho! Finalmente! Eu acho?']
derrotaCase = ["Eu sei que má notícia gosta de companhia, mas as minhas andam de mutirão.",
               "2. Na mala da vida, eu sou o xampu que abre a tampa e sai sujando e estragando tudo.",
               "3. De longe você parecia feio, de perto você parece que está de longe.",
               "4. É por isso que ninguém sentava contigo no recreio!",
               "5. Seu problema foi deixar a impressora perceber que você estava com pressa.",
               "6. Está vendo o carro novo do seu chefe? Se você seguir trabalhando com todo esse empenho, em seis meses ou um ano, ele vai conseguir comprar outro.",
               "7. A gente deveria receber adicional humilhação.",
               "8. Tudo saindo conforme o não planejado.",
               "9. Vai dar certo! Errado já está dando.",
               "10. Veja pelo lado bom: não há!",
               "11. A vida é um pêndulo entre o \"me deu mal\" e o \"me ferrei\".",
               "12. Na hora certa, tudo vai dar errado.",
               "13. Para quem já está humilhado, o que é mais uma derrota?",
               "14. É verdade essa mentira!",
               "15. É por isso que, na hora de apresentar o trabalho, você só segurava a cartolina.",
               "16. Estamos no ápice! No ápice do lascar.",
               "17. Vamos nos desesperar com calma.",
               "18. Essa vergonha você vai passar no cartão ou no débito?",
               "19. (Ch)oremos!",
               "20. Tudo certo para dar errado!",
               "21. Vamos rir, porque chorar entope o nariz e sua voz fica muito feia.",
               "22. É um absurdo, mas faz sentido.",
               "23. Eu esperava o pior, mas isso foi bem pior do que eu esperava.",
               "24. O mérito da derrota é todo seu, orgulhe-se.",
               "25. Olha... sério... na moral... sinceramente... sem condições.",
               "26. Por causa de gente como você que na caixa de ovo vem escrito \"Contém ovo\".",
               "27. Na cozinha da vida eu só sei fritar ovo e, de vez em quando, ainda queimo.",
               "28. Eu até tento esquecer meus problemas, mas eles parecem que não se esquecem de mim.",
               "29. É como diz o ditado: agora deu ruim!",
               "30. Faça uma vez, erre uma vez. Faça de novo, erre de novo.",
               "31. Vocês são as amizades que minha mãe pediu para eu evitar.",
               "32. A vida é 10% o que acontece com você e 90% o que aconteceria se você tivesse dinheiro.",
               "33. Se alguém quiser me derrubar hoje, vai ter que me ajudar a levantar primeiro porque eu já estou no chão.",
               "34. Se minha vida fosse um dia da semana, eu seria uma segunda-feira pós feriadão.",
               "35. Não sabendo que era impossível, foi lá e soube.",
               "36. Ouvi falar que cada um carregava sua cruz, mas a vida está achando que eu sou caminhão de frete e passando umas a mais para mim.",
               "37.Relaxe, está tudo absolutamente fora do seu controle.",
               "38. Estou doida para ganhar na loteria e poder postar foto com legenda sobre a felicidade estar nas coisas simples.",
               "39. Na subida para meu sucesso, o elevador está quebrado, a escada está escorregadia e, de vez em quando, passa alguém subindo apressado e quase me derrubando no caminho.",
               "40. Você não pode mudar o seu passado, mas pode estragar seu futuro.",
               "41. O cartão de crédito está aí para quebrar seu galho. Aí depois ele pega o galho e dá bem na sua cabeça.",
               "42. A cada dia que passa, está sobrando mais mês no fim do dinheiro.",
               "43. A recompensa pelo bom trabalho é mais trabalho.",
               "44. Nunca desista, faça até dar errado.",
               "45. A vida é um lindo conto de falhas.",
               "46. A inteligência artificial só não é mais incrível do que a burrice natural.",
               "47. Tudo aquilo que você passou até agora está te preparando para algo pior.",
               "48. Um dia você perde. No outro você não ganha.",
               "49. Ano novo, vida nova e mais 365 oportunidades de fazer besteira.",
               "50. Procrastinar é acreditar no potencial do seu \"eu\" de amanhã e se enganar por vários dias seguidos.",
               "51. Errar uma vez é humano. Repetir o erro só eu mesmo.",
               "52. Na viagem da vida, meu GPS está quebrado, estou sem co-piloto e o carro bem que precisa de uma revisão."]
if player == jogo:
    time.sleep(0.5)
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    time.sleep(1)
    print('Empatamos!')
    time.sleep(1)
    pergunta = int(input('Quer jogar de novo?(1-Sim/2-Não)\nR: '))
    if pergunta == 1:
        time.sleep(1)
        os.system('cls')
    elif pergunta == 2:
        time.sleep(1)
        print('Tudo bem, obrigado por jogar!')
    else:
        time.sleep(1)
        print('Entrada inválida!')
elif player == 1 and jogo == 3:
    time.sleep(0.5)
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    time.sleep(1)
    print(f'Minha jogada: {jogo}')
    time.sleep(1)
    print('Ahhhh não, eu perdi! Hahahhahaha')
    time.sleep(1)
    pergunta = int(input('Quer jogar de novo?(1-Sim/2-Não)\nR: '))
    if pergunta == 1:
        time.sleep(1)
        os.system('cls')
        print('Tudo bem, obrigado por jogar!')
    else:
        time.sleep(1)
        print('Entrada inválida!')
elif player == 1 and jogo == 2:
    time.sleep(0.5)
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    time.sleep(1)
    print(f'Minha jogada é: {jogo}')
    time.sleep(1)
    print(f'Caramba! KKKkkkk\n...{random.choice(vitoriaCase)}...')
    time.sleep(1)
    print('Mas é isso kkkkkkkkkk, eu consegui ganhar velho! Finalmente! Eu acho?')
    time.sleep(1)
    pergunta = int(input('Quer jogar de novo?(1-Sim/2-Não)\nR: '))
    if pergunta == 1:
        os.system('cls')
    elif pergunta == 2:
        print('Tudo bem, obrigado por jogar!')
    else:
        print('Entrada inválida!')
elif player == 2 and jogo == 1:
    time.sleep(0.5)
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    time.sleep(1)
    print('Hahhahaha! Pedra ganha de papel! Boa!')
    time.sleep(1)
    pergunta = int(input('Quer jogar de novo?(1-Sim/2-Não)\nR: '))
    if pergunta == 1:
        time.sleep(1)
        os.system('cls')
    elif pergunta == 2:
        time.sleep(1)
        print('Tudo bem, obrigado por jogar!')
    else:
        time.sleep(1)
        print('Entrada inválida!')
elif player == 2 and jogo == 3:
    time.sleep(0.5)
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    time.sleep(1)
    print(f'{random.choice(vitoriaCase)}')
    pergunta = int(input('Quer jogar de novo?(1-Sim/2-Não)\nR: '))
    if pergunta == 1:
        time.sleep(1)
        os.system('cls')
    elif pergunta == 2:
        time.sleep(1)
        print('Tudo bem, obrigado por jogar!')
    else:
        time.sleep(1)
        print('Entrada inválida!')
elif player == 3 and jogo == 2:
    time.sleep(0.5)
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    time.sleep(1)
    print(f'{random.choice(derrotaCase)}')
    pergunta = int(input('Quer jogar de novo?(1-Sim/2-Não)\nR: '))
    if pergunta == 1:
        time.sleep(1)
        os.system('cls')
    elif pergunta == 2:
        time.sleep(1)
        print('Tudo bem, obrigado por jogar!')
    else:
        time.sleep(1)
        print('Entrada inválida!')
elif player == 3 and jogo == 1:
    time.sleep(0.5)
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    time.sleep(1)
    print(f'{random.choice(vitoriaCase)}')
    pergunta = int(input('Quer jogar de novo?(1-Sim/2-Não)\nR: '))
    if pergunta == 1:
        time.sleep(1)
        os.system('cls')
    elif pergunta == 2:
        print('Tudo bem, obrigado por jogar!')
    else:
        print('Entrada inválida!')
        time.sleep(1)
    print('ERRO! O programa está na fase beta!')
# pedra 1
# papel 2
# tesoura 3
"""player = int(input('Qual você escolhe?\n'
'1-Pedra, 2-Papel, 3-Tesoura\n'
'Eu vou jogar: '))
jogo = random.randint(1, 3)
if player == jogo:
    print('Empatamos!')
elif player == 1 and jogo == 3:
    print()
elif player == 2:
    print('Você lançou papel!')

elif player == 3:
    print('Você lançou tesoura!')
"""
