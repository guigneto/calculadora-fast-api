def soma(a: float, b: float) -> float:
    return a + b

def subtracao(a: float, b: float) -> float:
    return a - b

def multiplicacao(a: float, b: float) -> float:
    return a * b

def divisao(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisão por zero")
    return a / b

def exponenciacao(a: float, b: float) -> float:
    return a ** b