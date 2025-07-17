
def delta (b,c,a):
    return b**2 - 4*a*c 
delta(-11, 2, 5)

def baskara (b,c,a):
    d = delta(b,c,a)
    if d < 0:
        return "Não existem raízes reais"
    elif d == 0:
        x = -b / (2 * a)
        return f"Apenas uma raiz: {x}"
    else:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        return f"duas raizes {x1} e {x2}"