from listaligada import *

def calcula_lista(l1: lista_ligada, no: no) -> int:
    '''

    '''
    if l1.lista_vazia():
        soma = 0
    else:
        soma = no.info + calcula_lista(l1, no.prox)
    return soma


def main():
    l1 = lista_ligada()

if __name__ == '__main__':
    main()