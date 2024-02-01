num = int(input('Digite um número: '))
if num > 1:
    for c in range(2, num):
        if num % c == 0:
            print(num, "não é primo.")
            break
    else:
        print(f'{num} é primo.')