def fibonacci(n: int, frase: str = '') -> str:
    if n == 1:
        return "0"
    elif n == 2:
        return "0, 1"
    else:
        # Chama recursivamente para construir a sequência anterior
        frase = fibonacci(n - 1)
        # Divide a sequência em uma lista de números
        partes = frase.split(", ")
        # Calcula o próximo número da sequência
        proximo = int(partes[-1]) + int(partes[-2])
        # Retorna a sequência atualizada como string
        return frase + ", " + str(proximo)


print(fibonacci(5))