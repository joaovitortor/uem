from listaligada import *

def calcula_lista(l1: lista_ligada, no: no) -> int:
    '''

    '''
    if no.prox == None:
        soma = 0
    else:
        soma = l1.primeiro.info + calcula_lista(l1.primeiro.prox)
    return soma

def main():
    l1 = lista_ligada()
    lista = [1, 2, 3, 4, 5]
    for i in lista:
        l1.insere_inicio(i)
    
    
    print(l1.calcula(l1.primeiro))
    

if __name__ == "__main__":
    main()