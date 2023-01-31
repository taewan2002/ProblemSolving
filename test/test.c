#include <stdio.h>
#include <string.h>

int f(n, start){
    if (n == start){
        return 0;
    }
    else{
        for(int i=0; i<start+1; i++){
            printf("*");
        }
        printf("\n");
        return f(n, start+1);
    }
}

int main(){
    int n;
    scanf("%d", &n);
    f(n, 0);
    return 0;
}         