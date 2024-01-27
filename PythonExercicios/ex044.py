preço = 400
pergunta = int(input(f'Qual vai ser o método de pagamento para o produto de R${preço}?\nOpções:\n'
'1- À vista dinheiro/cheque: 10% desconto\n'
'2- À vista no cartão: 5% de desconto\n'
'3- Em até 2x no cartão: preço normal\n'
'4- 3x ou mais no cartão: 20% de juros\nR: '))
if pergunta == 1:
    preçoFinal = preço + (preço * 10 / 100)
    print(f'Parabéns! Você tem 10% de desconto, o preço vai ser: \"R${preçoFinal}\"\nFim!')
elif pergunta == 2:
    preçoFinal = preço + (preço * 5 / 100)
    print(f'Parabéns, você ganha 5% de desconto. Preço final: \"R${preçoFinal}\"\nFim!')
elif pergunta == 3:
    print(f'O preço final vai ser de: \"R${preço}\"\nObrigado, volte sempre!')
elif pergunta == 4:
    prestaçao = preço * 20 / 100 + preço
    print(f'Hmmm, 3 vezes no cartão? É pra já...R${prestaçao} por mês.\n'
          f'Resultando um total de {prestaçao * 3}. Tenha um bom dia!')
else:
    print('Entrada inválida!')