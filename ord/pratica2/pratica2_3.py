import io
def leia_reg(entrada: io.BufferedReader) -> str:
    tam = entrada.read(2)
    tamint = int.from_bytes(tam)
    if tamint > 0:
        buffer = entrada.read(tamint)
        buffer.decode()
        return buffer.decode()
    else:
        return ''

nome_arq = input('Qual o nome do arquivo? ')
entrada = open(nome_arq, 'rb')
buffer = leia_reg(entrada)
msgs = ['Sobrenome: ', 'Nome: ', 'Endereço: ', 'Cidade: ', 'Estado: ', 'CEP: ', '']
j = 1
while buffer != '':
    campos = buffer.split(sep='|')
    i = 0
    print(f'Registro #{j}')
    j += 1
    for campo in campos:
        print(msgs[i] + campo)
        i += 1

    buffer = leia_reg(entrada)
    
entrada.close
