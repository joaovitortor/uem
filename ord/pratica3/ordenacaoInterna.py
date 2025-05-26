from sys import argv

def leia_registros(nome_arq_entrada: str) -> list[tuple[int, bytes]]:
    registros: list[tuple[int, bytes]]
    registros = []
    with open(nome_arq_entrada, 'rb') as entrada:
        #Ler cabeçalho
        num_registros = int.from_bytes(entrada.read(4))

        #Repetir para todos os registros
        for _ in range(num_registros):
            #Ler tamanho do registro
            tamanho_bytes = entrada.read(2)
            tamanho = int.from_bytes(tamanho_bytes)

            #Ler registro
            registro_bytes = entrada.read(tamanho)
            registro = registro_bytes.decode()

            #Separar campos na '|'
            campos = registro.split(sep = '|')

            #Guarda o identificador e os dados binários do registro p/ reescrever depois
            registros.append((int(campos[0]), tamanho_bytes+registro_bytes))

    return registros

def escreva_registros_ordenados(nome_arq_saida: str, registros: list[tuple[int, bytes]]) -> None:
    with open(nome_arq_saida, 'wb') as f:
        #Escrever o cabeçalho com o número de registros
        f.write(len(registros).to_bytes(4))

        #Escrever os registros ordenados
        for _, registro_bytes in registros:
            f.write(registro_bytes)

def ordene_arquivo_por_identificador(nome_arq_entrada: str, nome_arq_saida: str) -> None:
    #Ler os registros para a lista registros
    registros = leia_registros(nome_arq_entrada)

    #Ordena por identificador (assumindo que ele é o primeiro campo e um inteiro)
    registros.sort()

    #Escrever os registros no arquivo e saída na ordem da lista de registros
    escreva_registros_ordenados(nome_arq_saida, registros)

def main() -> None:
    if len(argv) < 3:
        raise TypeError('Número incorreto de argumentos \n Modo de uso: nome_arq_entrada nome_arq_saida')
    ordene_arquivo_por_identificador(argv[1], argv[2])

if __name__ == '__main__':
    main()
        







