#include <stdio.h>

int main(){
    int v[10], i;
    printf("v: %p\n",v);
    printf("&v: %p\n",&v);
    printf("&v[0]: %p\n",&v[0]);
    for(i=0; i<10; i++){
        printf("&v[%d]: %p\n",i,&v[i]);
    }
}