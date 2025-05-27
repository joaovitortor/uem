#Faça uma função que receba um vetor de inteiros e que calcule recursivamente a soma de todos os elementos do vetor

def calcula_vetor(lista: list[int]) -> int:
    '''
    >>> calcula_vetor([1,2,3,4,5])
    15
    '''
    if not lista:
        soma = 0
    else:
        soma = lista[0] + calcula_vetor(lista[1:])
    return soma