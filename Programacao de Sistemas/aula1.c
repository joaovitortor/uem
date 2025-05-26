#include <stdio.h>

int main(){
    int m[5][3] = {{0,0,0}, {0,0,0}, {0,0,0}, {0,0,0}, {0,0,0}};
    int i, j;
    for(i=0; i < 5; i++){
        for(j=0; j < 3; j++){
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }
}
