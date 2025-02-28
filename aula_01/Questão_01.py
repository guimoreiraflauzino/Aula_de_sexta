
numero = input("Digite um número de 5 dígitos: ")


if len(numero) == 5 and numero.isdigit():
    
    print("   ".join(numero))
else:
    print("Por favor, insira um número válido de 5 dígitos.")
