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
    # Tenta ler 2 bytes para o tamanho do registro
    tam_bytes = arq.read(SIZEOF_TAMREG) 
    
    # Se não leu 2 bytes (significa que chegou ao fim do arquivo ou o arquivo é menor que 2 bytes)
    if len(tam_bytes) < SIZEOF_TAMREG:
        return ('', 0) # Retorna um registro vazio com tamanho 0, indicando EOF
    
    tam = unpack('h', tam_bytes)[0]
    if tam > 0:
        registro = arq.read(tam).decode()
        return(registro, tam)
    else:
        return('', 0)
    


def constroi_indice(arq: io.BufferedReader) -> list[(int, int)]:
    chaves: list[tuple[int, int]] = []
    
    # Lê o primeiro registro fora do loop
    current_offset = arq.tell()
    registro, tam_registro = leia_reg(arq)
    
    # O loop continua enquanto o tamanho do registro não for zero (ou seja, enquanto houver registros válidos)
    while tam_registro != 0:
        campos = registro.split('|')
        # Adiciona a chave e o offset onde o registro *começa*
        chaves.append((int(campos[0]), current_offset)) 
        
        # Prepara para a próxima iteração: lê o próximo registro e atualiza o offset
        current_offset = arq.tell()
        registro, tam_registro = leia_reg(arq)
        
    return chaves

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
    nomearq = input("Digite o nome do arq: ")
    with open('trabalhos.dat', 'rb') as entrada:
        entrada.read(4)
        chaves = constroi_indice(entrada)
        print(chaves)



if __name__ == '__main__':
    main()


#pensar melhor