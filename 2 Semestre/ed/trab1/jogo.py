from pilha import *
from random import shuffle

def mostra_pilhas(pilhas: list[pilha]):
    '''
    Exibe todas as pilhas numeradas e seus elementos.
    '''
    print("=================================")
    for i in range(len(pilhas)):
        print(f"Pilha {i+1}: [", end="")
        for j in range(4):
            if j > pilhas[i].topo-1:
                print("_ ", end="")
            elif j < 3: 
                print(str(pilhas[i].elementos[j]) + ", ", end="")
            else:
                print(str(pilhas[i].elementos[j]), end="")
        print("]")

def move_elemento(pilhas: list[pilha], p1: int, p2: int):
    '''
    Verifica se é possível movimentar o elemento do topo da pilha na posição *p1* para a posição *p2* e, se possível, realiza o movimento.
    Para movimentar é necessário verificar se a pilha onde está o elemento não está vazia, se a pilha destino do elemento não está cheia, e se
    o elemento do topo da pilha destino é igual o elemento que está sendo movido ou se é igual a None.
    '''
    if len(pilhas) - 1 >= p1 and len(pilhas) - 1 >= p2:
        if pilhas[p1].vazia():
            print("Movimento inválido: pilha de origem está vazia.")
        elif pilhas[p2].cheia():
            print("Movimento inválido: pilha de destino está cheia.")
        elif pilhas[p2].vazia() or pilhas[p1].consulta_topo() == pilhas[p2].consulta_topo():
            x = pilhas[p1].desempilha()
            if x is not None:
                pilhas[p2].empilha(x)
        else: 
            print("Movimento inválido: os elementos são diferentes")
    else: 
        print("Movimento inválido. Pilha não existe")

def verifica_vitoria(pilhas: list[pilha]) -> bool:
    '''
    Verifica se o jogo foi vencido e retorna True, ou retorna False caso contrario.
    Para ganhar o jogo é necessário que tenha duas pilhas vazias e que todas as outras pilhas estejam com os mesmos elementos
    '''
    continua = True
    n = 0
    vazia = 0

    while continua and n < len(pilhas):
        if pilhas[n].cheia():
            i = 1
            while i < pilhas[n].topo and continua:
                continua = pilhas[n].elementos[0] == pilhas[n].elementos[i]
                i += 1  
        elif pilhas[n].vazia():
            vazia += 1
        n += 1  

    return continua and vazia == 2

def cria_pilhas(num_pilhas) -> list[pilha]:
    '''
    Retorna uma lista de pilhas, com as primeiras *num_pilhas - 2* contendo uma permutação dos números de 1 até *num_pilhas*, repetidos 4 vezes.
    '''
    pilhas: list[pilha] = []
    for _ in range(num_pilhas):
        pilhas.append(pilha(4))


    lista: list[int] = []
    for i in range(1, num_pilhas-1):
        lista.append(i)
    
    lista = lista*4

    shuffle(lista)
    k = 0
    i = 0
    while k < len(lista):
        for _ in range(4):
            pilhas[i].empilha(lista[k])
            k += 1
        i += 1

    return pilhas

def verifica_numero(num: str, tam_max) -> bool:
    '''
    Verifica se *num* é um número inteiro e se está dentro do intervalo válido retornando True caso for e False caso contrário.
    '''
    return num.isdigit() and 1 <= int(num) <= tam_max


def main():
    print("Bem-vindo ao jogo feito pelo João Bidoia e Pedro Henrique")
    num_pilhas = int(input("Digite a dificuldade desejada (de 1 a 7): ")) + 2
    while not (1 <= num_pilhas <= 9):
        print("Digite um número válido")
        num_pilhas = int(input("Digite a dificuldade desejada (de 1 a 7): ")) + 2

    pilhas = cria_pilhas(num_pilhas)
    continua = True
    mostra_pilhas(pilhas)
    if verifica_vitoria(pilhas):
        continua = False
    while continua:

        p1 = input("De qual pilha você quer tirar? ")
        while not verifica_numero(p1, num_pilhas):
            print("Entrada inválida! Digite um número válido.")
            p1 = input("De qual pilha você quer tirar? ")
        p1 = int(p1) - 1

        p2 = input("Em qual pilha você quer adicionar? ")
        while not verifica_numero(p2, num_pilhas):
            print("Entrada inválida! Digite um número válido.")
            p2 = input("Em qual pilha você quer adicionar? ")
        p2 = int(p2) - 1
        
        move_elemento(pilhas, p1, p2)
        
        mostra_pilhas(pilhas)
        
        if pilhas[p2].cheia() and pilhas[p1].vazia():
            continua = not verifica_vitoria(pilhas)

    print("Você ganhouuuuuu")
    

if __name__ == "__main__":
    main()