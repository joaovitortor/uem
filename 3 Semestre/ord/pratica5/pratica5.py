from struct import pack, unpack, calcsize
import io
import os

# CONSTANTES
FORMATO_ELEMINDICE = '2i'   # dois inteiros de 4 bytes
FORMATO_HEADER = 'i'        # um inteiro de 4 bytes
FORMATO_TAMREG = 'h'        # um inteiro de 2 bytes
SIZEOF_ELEMINDICE = calcsize(FORMATO_ELEMINDICE)    # 8 bytes
SIZEOF_HEADER = calcsize(FORMATO_HEADER)            # 4 bytes
SIZEOF_TAMREG = calcsize(FORMATO_TAMREG)            # 2 bytes

# por padrão, as funções do módulo struct representam os dados em formato 'little endian'
# para facilitar, o arquivo 'trabalhos.dat' também foi gravado em formato 'little endian'

def leia_reg(arq: io.BufferedReader) -> tuple[str, int]:
    tamanho = unpack(FORMATO_TAMREG, arq.read(SIZEOF_TAMREG))[0]
    if tamanho > 0:
        registro = arq.read(tamanho).decode()
        return (registro, tamanho)
    return ('', 0)

def constroi_indice(arq: io.BufferedReader) -> list[tuple[int, int]]:
    '''
    forma uma tupla com os ids e os offsets
    '''
    num_registros = unpack(FORMATO_HEADER, arq.read(SIZEOF_HEADER))[0]
    chaves: list[tuple[int, int]] = []
    for _ in range(num_registros):
        offset = arq.tell()
        dados, tamanho = leia_reg(arq)
        id = int((dados.split('|'))[0])
        chaves.append((id, offset))
    chaves.sort()
    return chaves

def grava_indice(indice: list[tuple[int, int]]) -> None:
    saida = open('indice.dat', 'wb')
    quant_elem = len(indice)
    saida.write(pack(FORMATO_HEADER, quant_elem))
    for elem in indice:
        saida.write(pack(FORMATO_ELEMINDICE, *elem))

def carrega_indice() -> list[tuple[int, int]]:
    indices = open('indice.dat', 'rb')
    chaves: list[tuple[int, int]] = []
    quant_elem = unpack(FORMATO_HEADER, indices.read(SIZEOF_HEADER))[0]
    for _ in range(quant_elem):
        id = unpack(FORMATO_HEADER, indices.read(SIZEOF_HEADER))[0]
        offset = unpack(FORMATO_HEADER, indices.read(SIZEOF_HEADER))[0]
        chaves.append((id, offset))
    return chaves


def busca_binaria(chave: int, indice: list[tuple[int, int]]) -> int:
    i = 0
    f = len(indice) - 1
    while i <= f:
        m = (i + f)//2
        if indice[m][0] == chave:
            return m
        if indice[m][0] < chave:
            i = m + 1
        else: 
            f = m - 1
    return -1

   

def le_e_imprime(arq: io.BufferedReader, offset: int) -> None:
    arq.seek(offset)
    dados, tamanho = leia_reg(arq)
    registros = dados.split('|')
    for registro in registros:
        print(registro)



def imprime_indice(indice: list[tuple[int, int]]) -> None:
    pass

def main() -> None:
    #falta melhorar a main()
    entrada = open('trabalhos.dat', 'rb')
    indices = constroi_indice(entrada)
    print(indices)
    grava_indice(indices)

    print("------------------------")
    indices1 = carrega_indice()
    print(indices1)

    busca = busca_binaria(110, indices)
    print(busca)

    le_e_imprime(entrada, 4)

if __name__ == '__main__':
    main()