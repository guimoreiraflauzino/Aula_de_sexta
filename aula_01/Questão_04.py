def hanoi(n, origem, destino, auxiliar):
    # Caso base: se há apenas 1 disco, basta movê-lo
    if n == 1:
        print(f"Movendo o disco 1 de {origem} para {destino}")
    else:
        # Passo 1: mover os n-1 discos da origem para a auxiliar
        hanoi(n-1, origem, auxiliar, destino)
        
        # Passo 2: mover o maior disco da origem para o destino
        print(f"Movendo o disco {n} de {origem} para {destino}")
        
        # Passo 3: mover os n-1 discos da auxiliar para o destino
        hanoi(n-1, auxiliar, destino, origem)

# Solicitar ao usuário o número de discos
n = int(input("Digite o número de discos: "))

# Chamar a função recursiva com as torres de origem 'A', destino 'C' e auxiliar 'B'
hanoi(n, 'A', 'C', 'B')
