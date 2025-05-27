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
    


def constroi_indice(arq: io.BufferedReader) -> list[(int, int)]:
    pass

def grava_indice(indice: list[(int, int)]) -> None:
    pass

def carrega_indice() -> list[(int, int)]:
    pass


def busca_binaria(chave: int, indice: list[(int, int)]) -> int:
    pass
   

def le_e_imprime(arq: io.BufferedReader, offset: int) -> None:
    pass

def imprime_indice(indice: list[(int, int)]) -> None:
    pass

def main() -> None:
    pass       

if __name__ == '__main__':
    main()