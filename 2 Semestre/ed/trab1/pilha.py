from __future__ import annotations
from dataclasses import dataclass

@dataclass
class pilha:
    def __init__(self, tam_max: int):
        '''
        Inicializa a pilha, armazenando o tamanho máximo da pilha, declarando o topo igual a 0 e todos os elementos da pilha como None
        '''
        self.elementos: list[int | None] = [None] * tam_max
        self.tam_max = tam_max
        self.topo = 0

    def vazia(self) -> bool:
        '''
        Verifica se a pilha está vazia retornando True caso estiver e False caso contrário.
        Para a pilha estar vazia, o topo tem que ser igual a zero
        '''
        return self.topo == 0
    
    def cheia(self) -> bool:
        '''
        Verifica se a pilha está cheia retornando True caso estiver e False caso contrário.
        Para a pilha estar vazia, o topo tem que ser igual ao tamanho máximo
        '''
        return self.topo == self.tam_max

    def empilha(self, x: int):
        '''
        Insere um valor na pilha, ou seja, insere o elemento no topo da lista e incrementa o topo.
        Antes de inserir é necessário verificar se a pilha não está cheia
        '''
        if self.cheia():
            raise ValueError('Pilha Cheia')
        else:
            self.elementos[self.topo] = x
            self.topo += 1
    
    def desempilha(self) -> int | None:
        '''
        Remove um valor na pilha, ou seja, remove o elemento no topo da lista e decrementa o topo.
        Antes de remover é necessário verificar se a pilha não está vazia
        '''
    
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            x = self.elementos[self.topo-1]
            self.topo -= 1
            return x
            
    def consulta_topo(self) -> int | None:
        '''
        Retorna qual elemento está no topo da pilha sem removê-lo.
        >>> p = pilha(4)
        >>> p.empilha(11)
        >>> p.consulta_topo()
        11'''
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            return self.elementos[self.topo-1]