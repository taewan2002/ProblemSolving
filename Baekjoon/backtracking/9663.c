#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int n_queen(int x, int y, int *x_list, int *y_list, int n){
    int count = 0;
    for(int i=0; i<y; i++)
        if(x_list[i] == x || y_list[i] == y || abs(x_list[i] - x) == abs(y_list[i] - y)) return 0;
    if(y == n-1) return 1;
    x_list[y] = x;
    y_list[y] = y;
    for(int i=0; i<n; i++){
        count += n_queen(i, y+1, x_list, y_list, n);
    }
    return count;
}

int main(){
    int n, cnt=0;
    int y=0;
    scanf("%d", &n);
    int *x_list = (int*)malloc(sizeof(int)*n);
    int *y_list = (int*)malloc(sizeof(int)*n);
    for(int x=0; x<n; x++){
        cnt += n_queen(x, y, x_list, y_list, n);
    }
    printf("%d\n", cnt);
}