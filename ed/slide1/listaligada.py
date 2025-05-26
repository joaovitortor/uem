from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass

class no:
    def __init__(self, x):
        self.info = x
        self.prox: no | None = None
    
class lista_ligada:
    def __init__(self):
        self.primeiro: no | None = None
        self.ultimo:  no | None = None
    
    def lista_vazia(self) -> bool:
        return self.primeiro == None
    
    def insere_inicio(self, x):
        if self.busca(x) == None:
            novo = no(x)
            if self.lista_vazia():
                self.ultimo = novo
            novo.prox = self.primeiro
            self.primeiro = novo
    
    def busca(self, x) -> no | None:
        ponteiro = self.primeiro
        while (ponteiro is not None) and (ponteiro.info != x):
            ponteiro = ponteiro.prox
        return ponteiro
    
    def remove_primeiro(self):
        if not self.lista_vazia():
            ponteiro = self.primeiro
            self.primeiro = ponteiro.prox
            if self.lista_vazia():
                self.ultimo = None
            ponteiro.prox = None

    def remove_elemento(self, x):
        if self.busca(x) is not None:
            ponteiro = self.primeiro
            if ponteiro.info == x:
                self.remove_primeiro()
            else:
                while ponteiro.prox.info != x:
                    ponteiro = ponteiro.prox
                ref = ponteiro.prox
                ponteiro.prox = ref.prox
                ref.prox = None
    
    def calcula(self, no: no) -> int:
        if no == None:
            return 0
        else:
            return no.info + self.calcula(no.prox)
