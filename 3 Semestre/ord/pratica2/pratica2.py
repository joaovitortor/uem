import io
def leia_campos(ENTRADA: io.TextIOWrapper) -> str:
    campo: str = ''
    c = ENTRADA.read(1)
    while c not in ('', '|'):
        campo = campo + c
        c = ENTRADA.read(1)
    return campo

nome_arq = input('Qual o nome do arquivo? ')
try:
    ENTRADA = open(nome_arq, 'r')
    campo = leia_campos(ENTRADA)
    i = 1
    while campo != '':
        print(f'Campo #{i}: {campo}')
        i += 1
        campo = leia_campos(ENTRADA)
    ENTRADA.close()
except FileNotFoundError as e:
    print(f'Erro: {e}')






