mostrar = int(input('Quantos digitos ? '))

n1 = 0
n2 = 1

print(f'{n1}, {n2}, ', end='')  # Mostro o 0, 1 pois sempre serão o inicio da sequencia

contador = 2  # Inicio o contador no 2 pois ja possuo os 2 primeiros algarismos

while contador < mostrar:  # Inicio aqui o laço que é responsavel por printar o n3 na posição correta e na sequencia igualar o n1 a n2 e n2 a n3
    n3 = n1 + n2
    print(f'{n3}, ', end='')  # O end é usado para o print não pular linha
    mostrar -= 1
    n1 = n2
    n2 = n3
print('FIM')