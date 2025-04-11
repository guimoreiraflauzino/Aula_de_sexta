def sequencia(n, memo={}):
    if n==0:
        return 0
    if n==1:
        return 1

    resultado =  sequencia(n-1,memo)+2*sequencia(n-2,memo)
    memo[n]= resultado
    
    print(memo)

    return resultado
n=int(input("enre com uma posição"))

print(f"T{(n)} = {sequencia(n)}")