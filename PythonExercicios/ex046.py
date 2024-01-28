import time

print('Prepare-se para a explosão dos fogos!')
for c in range(10, -1, -1):
    time.sleep(1)
    print(c, '...')
    if c == 0:
        print('FELIZ ANO NOVO!!! 🎆')
        time.sleep(1)
print('Fim!')