nome_arq = input('Qual o nome do arquivo? ')
saida = open(nome_arq, 'wb')
campo = input('Sobrenome: ')
msgs = ['Nome: ', 'Endereço: ', 'Cidade: ', 'Estado: ', 'CEP: ']
while campo != '':
    buffer = ''
    buffer = campo + '|'
    for msg in msgs:
        campo = input(msg)
        buffer = buffer + campo + '|'
    bufferb = buffer.encode()
    tam = len(buffer)
    tamb = tam.to_bytes(2)
    saida.write(tamb)
    saida.write(bufferb)
    campo = input('Sobrenome: ')
saida.close()



