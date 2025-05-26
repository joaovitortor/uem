nomeArq = input('Qual o nome do arquivo? ')
SAIDA = open(nomeArq, 'w')
DADOS: list[str] = []
DADOS.append(input('Sobrenome: '))
msgs = ['Nome: ', 'Endereço: ', 'Cidade: ', 'Estado: ', 'CEP: ']
while DADOS[0] != '':
    for msg in msgs:
        DADOS.append((input(msg)))
    for dado in DADOS:
        SAIDA.write(dado + '|')
    SAIDA.write('\n')
    DADOS = []
    DADOS.append(input('Sobrenome: '))
SAIDA.close