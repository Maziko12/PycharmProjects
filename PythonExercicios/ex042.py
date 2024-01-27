Seg1 = int(input('Primeiro segmento\nR: '))
Seg2 = int(input('Segundo segmento\nR: '))
Seg3 = int(input('Terceiro segmento\nR: '))
if Seg1 != Seg2 != Seg3:
    print('É possível criar um triângulo ESCALENO com esses segmentos!')
elif Seg3 == Seg2 == Seg1:
    print('Este triângulo, é um triângulo HEQUILÁTERO!')
elif Seg1 == Seg2 or Seg2 == Seg3 or Seg3 == Seg1:
    print('Este triângulo, é um triângulo ISÓSCELES!')
