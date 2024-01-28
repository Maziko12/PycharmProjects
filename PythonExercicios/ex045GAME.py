import random
import os
import time

player = int(input('Qual você escolhe?\n'
'1-Pedra, 2-Papel, 3-Tesoura\n'
'Eu vou jogar: '))
jogo = random.randint(1, 3)
Case = ["PEDRA", "PAPEL", "TESOURA"]
Esqueleto = [player, time.sleep(1), "-=" * 11, jogo,"-=" * 11, f"\nO Computador jogou {jogo}.\n",
              f"O Jogador jogou {player}.", "-=" * 11]
dataset = {
    "pedra": "True"
}

if player == jogo:
    print('Empatamos!')
elif player == 1 and jogo == 3:
    print()
elif player == 2:
    print('Você lançou papel!')

elif player == 3:
    print('Você lançou tesoura!')

if __name__ == "__main__":
    print('Setup!')