n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('A soma vale {} a multiplicação vale {} a divisão vale {:.2f} a' .format(s, m, d), end='')
print(' divisão inteira vale {} e a potência vale {}'.format(di, p))

