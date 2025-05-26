#include <stdio.h>

int main(){
    int a, *pont_int;
    char b, *pont_char;
    a = 5;
    b = '.';
    pont_int = &a;
    pont_char = &b;

    printf("Variavel de a: %d\n", a);
    printf("Endereco de a: %p\n", &a);
    printf("Ponteiro pont_int: %p\n", pont_int);
    printf("Conteudo do endereco apontado por pont_int: %d\n", *pont_int);

    printf("Variavel de b: %c\n", b);
    printf("Endereco de b: %p\n", &b);
    printf("Ponteiro pont_char: %p\n", pont_char);
    printf("Conteudo do endereco apontado por pont_char: %c\n", *pont_char);

}