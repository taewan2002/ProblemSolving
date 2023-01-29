#include <stdio.h>

int main(){
    int arr[5][5];
    int arr1[5][5];

    int n = 1;
    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++){
            arr[i][j] = n;
            n++;
        }
    }


    // arr -> arr1 뒤집어서 
    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++){
            arr[i][j] = n;
            n++;
        }
    }


    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++){
            printf("%d ", arr1[i][j]);
        }
        printf("\n");
    }

    return 0;
}         