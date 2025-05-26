#include <stdio.h>
int main(){
    int x, y, *p1, *p2, *p3;
    x = 10;
    y = 5;

    printf("x: %d, y: %d\n",x,y);
    p1 = &x; //p1 aponta para o endereco de memoria x
    *p1 = 99; //acessa o endereco de memoria apontado por p1 e coloca o valor 99
    printf("x: %d, y: %d\n",x,y);
    p1 = &y; //p1 aponta para o endereco de memoria y
    *p1 = 55; //acessa o endereco de memoria apontado por p1 e coloca o valor 55
    printf("x: %d, y: %d\n",x,y);
    p2 = &x; //p2 aponta para o endereco de memoria x
    *p2 = 88; //acessa o endereco de memoria apontado por p2 e coloca o valor 88
    printf("x: %d, y: %d\n",x,y);
    p3 = p1; //p3 aponta para o mesmo local que p1 aponta (y)
    p1 = p2; //p1 aponta para o mesmo local que p2 aponta (x)
    p2 = p3; //p2 aponta para o mesmo local que p3 aponta (y)
    printf("x: %d, y: %d\n",x,y);
    *p3 = 66;
    printf("x: %d, y: %d\n",x,y);
}