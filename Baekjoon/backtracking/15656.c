#include<stdio.h>
#include<stdlib.h>

void sort(int *result, int m){
    for(int i=0; i<m-1; i++){
        for(int j=i+1; j<m; j++){
            if(result[i] > result[j]){
                int temp = result[i];
                result[i] = result[j];
                result[j] = temp;
            }
        }
    }
}

void dfs(int depth, int n, int m, int *num_list, int *result){
    if(depth == m){
        for(int i=0; i<m; i++){
            printf("%d ", result[i]);
        }
        printf("\n");
    }
    else{
        for (int i = 0; i < n; i++){
            result[depth] = num_list[i];
            dfs(depth + 1, n, m, num_list, result);
        }
    }
}

int main(){
    int n, m;
    int *num_list = (int*)malloc(sizeof(int)*n);
    int *total_list = (int*)malloc(sizeof(int)*m);

    scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++){
        scanf("%d", &num_list[i]);
    }
    sort(num_list, n);
    dfs(0, n, m, num_list, total_list);
}