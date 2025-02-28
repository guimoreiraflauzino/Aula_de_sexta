
def quadrado_soma_impares(n):
    soma = 0
    for i in range(n):
        soma += (2*i + 1)  
    return soma


n = int(input("Digite um número natural: "))


resultado = quadrado_soma_impares(n)

print(f"O quadrado de {n} é {resultado}, que é a soma dos primeiros {n} números ímpares.")
