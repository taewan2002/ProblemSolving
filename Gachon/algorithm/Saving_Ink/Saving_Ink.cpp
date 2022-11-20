#include<stdlib.h>
#include<stdio.h>
#include<math.h>

double table[30][2];
double total[30];
int n, k=0;

void read_data(){
    /* read data and save the data */
    FILE* fb = fopen("input.txt", "r");
    if(fb==NULL){
        printf("Could not open input.txt!\n");
        exit(1);
    }
    
    fscanf(fb,"%d",&n);
    for(int i=0; i<n; i++)
        fscanf(fb, "%lf %lf", &table[i][0], &table[i][1]);
}

void processing(){
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            total[k++] = sqrt(pow(table[i][0] - table[j][0], 2) + pow(table[i][1] - table[j][1], 2));
        }
    }
    double temp, sum;
    for(int i=0; i<n-1; i++)
        for(int j=0; j<n-1-i; j++)
            if(total[j] > total[j+1]) {
                temp = total[j];
                total[j] = total[j+1];
                total[j+1] = temp;
            }
    for(int i=0; i<n-1; i++){
        sum += total[i];
    }
    printf("%.2f\n", sum);
}

int main(){
    read_data();
    processing();
	return 0;
}