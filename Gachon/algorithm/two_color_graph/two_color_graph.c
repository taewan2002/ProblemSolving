#include<stdio.h>
#include<stdlib.h>

int main(){
    FILE *fp = fopen("input.txt", "r");
    if(fp==NULL){
        printf("Could not open input.txt!\n");
        exit(1);
    }

    while (feof(fp) == 0){
        int n, m; // n: number of egded, m: number of vertex
        fscanf(fp, "%d %d", &n, &m);
        int **graph = (int **)malloc(sizeof(int*) * n);
        for(int i=0; i<n; i++){
            graph[i] = (int *)malloc(sizeof(int) * n);
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                graph[i][j] = 0;
            }
        }

        int a, b;
        for(int i=0; i<m; i++){
            // read data from input.txt
            fscanf(fp, "%d %d", &a, &b);
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        // two color graph
        int *color = (int *)malloc(sizeof(int) * m);
        for(int i=0; i<m; i++){
            color[i] = 0;
        }

        int *queue = (int *)malloc(sizeof(int) * m);
        int front = 0, rear = 0;
        int flag = 0;
        for(int i=0; i<m; i++){
            if(color[i] == 0){
                color[i] = 1;
                queue[rear++] = i;
                while(front != rear){
                    int v = queue[front++];
                    for(int j=0; j<m; j++){
                        if(graph[v][j] == 1){
                            if(color[j] == 0){
                                color[j] = -color[v];
                                queue[rear++] = j;
                            }
                            else if(color[j] == color[v]){
                                flag = 1;
                                break;
                            }
                        }
                    }
                    if(flag == 1){
                        break;
                    }
                }
            }
            if(flag == 1){
                break;
            }
        }

        if(flag == 1){
            printf("not two-color\n");
        }
        else{
            printf("two-color\n");
        }

    
        // free memory
        for(int i=0; i<m; i++){
            free(graph[i]);
        }
        free(graph);
        free(color);
        free(queue);
    }
    return 0;
}