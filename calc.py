def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("divisao por zero nao e permitida")
    return a / b


OPERACOES = {
    "+": somar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir,
}


def calcular(operacao, a, b):
    if operacao not in OPERACOES:
        raise ValueError(f"operacao invalida: {operacao}")
    return OPERACOES[operacao](a, b)


if __name__ == "__main__":
    resultado = calcular("*", 6, 7)
    print(f"6 * 7 = {resultado}")