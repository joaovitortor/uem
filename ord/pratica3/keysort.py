from sys import argv
import io

def leia_registros(nome_arq_entrada: str) -> list[tuple[int,int]]:
    chaves: list[tuple[int, int]] = []
    with open(nome_arq_entrada, 'rb') as entrada:
        #Ler o cabeçalho
        num_registros = int.from_bytes(entrada.read(4))

        #Calcular o offset do 1o registro
        offset = entrada.tell()

        #Repetir para todos os registros
        for _ in range(num_registros):
            #Ler tamaho do registro
            tamanho_bytes = entrada.read(2)
            tamanho = int.from_bytes(tamanho_bytes)

            #Ler registro
            registro_bytes = entrada.read(tamanho)

            #Separar os campos na '|'
            campos = registro_bytes.split(b'|')

            #Guardar o identificador e os dados binários p/ reescrever depois
            chaves.append((int(campos[0]), offset))

            #Guardar o offset do próximo registro
            offset += tamanho + 2

    return chaves

def escreva_registros_ordenados(nome_arq_entrada: str, nome_arq_saida: str, chaves: list[tuple[int,int]]) -> None:
    #Abrir os arquivos da entrada e escrever na saída
    with open(nome_arq_entrada, 'rb') as entrada, open(nome_arq_saida, 'wb') as saida:
        cabecalho = entrada.read(4)
        saida.write(cabecalho)

        #Escrever os registros de entrada ordenados em saída
        for _, offset in chaves:
            #Vá para o offset no arquivo de entrada e leia o registro
            entrada.seek(offset)
            tamanho_bytes = entrada.read(2)
            tamanho = int.from_bytes(tamanho_bytes)
            registro_bytes = entrada.read(tamanho)

            #Escreva o registro lido no arquivo de saída
            saida.write(tamanho_bytes + registro_bytes)

def keysort(nome_arq_entrada: str, nome_arq_saida: str) -> None:
    #Ler chaves e offsets do arquivo de entrada
    chaves = leia_registros(nome_arq_entrada)

    #Ordenar chaves (assumindo que o ID o primeiro campo e um inteiro)
    chaves.sort()

    #Escrever o arquivo de saída ordenado
    escreva_registros_ordenados(nome_arq_entrada, nome_arq_saida, chaves)

def main() -> None:
    if len(argv) < 3:
        raise TypeError('Número incorreto de argumentos \nModo de uso: nome_arq_entrada, nome_arq_saida')
    keysort(argv[1], argv[2])

if __name__ == '__main__':
    main()