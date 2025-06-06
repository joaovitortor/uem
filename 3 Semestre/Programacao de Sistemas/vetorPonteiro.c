#include <stdio.h>

int main(){
    int v[10] = {6, 2, 1, 9, 4};
    int *pv = v;
    int i;
    for(i=0; i<5; i++){
        printf("pv[%d] = %d\n",i,pv[i]);
    }
    i = 99;
    pv = &i;
    printf("pv[0] = %d\n", pv[0]);
    printf("pv[1] = %d", pv[1]);
}