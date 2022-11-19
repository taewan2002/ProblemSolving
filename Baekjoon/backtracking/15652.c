#include<stdio.h>
#include<stdlib.h>

int check_upperbound(int *result, int m){
    for(int i=0; i<m-1; i++){
        if(result[i] > result[i+1]){
            return 0;
        }
    }
    return 1;
}

void dfs(int depth, int n, int m, int *result){
    if(depth == m){
        if(check_upperbound(result, m)){
            for(int i=0; i<m; i++){
                printf("%d ", result[i]);
            }
            printf("\n");
        }
    }
    else{
        for (int i = 0; i < n; i++){
            result[depth] = i + 1;
            dfs(depth + 1, n, m, result);
        }
    }
}

int main(){
    int n, m;
    int *total_list = (int*)malloc(sizeof(int)*m);
    scanf("%d %d", &n, &m);
    dfs(0, n, m, total_list);
}