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
    # lista_campos: list[str] = []
    # i = 1
    # linha_campos = ENTRADA.readline()
    # while linha_campos != '':
    #     lista_campos.append(linha_campos)
    #     linha_campos = ENTRADA.readline()
    # for elem_campo in lista_campos:
    #     campo = elem_campo.split('|')
    #     print(f'Pessoa {i}')
    #     print(f'Sobrenome: {campo[0]}')
    #     print(f'Nome: {campo[1]}')
    #     print(f'Endereco: {campo[2]}')
    #     print(f'Cidade: {campo[3]}')
    #     print(f'CEP: {campo[4]} \n')
    #     i += 1
    for linha in ENTRADA:
        # Sobrenome, nome, end, cid, est, cep = linha.split(sep='|')
        for campo in linha.split(sep='|'):
            print(campo)
except FileNotFoundError as e:
    print(f'Erro: {e}')