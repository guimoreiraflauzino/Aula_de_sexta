def suc(n):
    # Sucessor de n (n + 1)
    return n + 1

def pred(n):
    # Predecessor de n (n - 1)
    return n - 1

def soma(n, m):
    if m == 0:
        return n
    else:
        return suc(soma(n, pred(m)))
