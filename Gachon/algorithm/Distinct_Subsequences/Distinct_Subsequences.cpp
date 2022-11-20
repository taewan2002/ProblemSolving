#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int subStance(int matrix[][100], char compareWord[100], char word[100]);

int main(){
    int cntData = 0; // how many a pair of data in file
    char compareWord[100], word[100];
    int matrix[100][100] = { 0 }; // initailize 100 by 100 matirx to 0

    /* Load File */
    FILE* fp;
    fp = fopen("input.txt", "r");
    if (fp == NULL) { // Check availiable file
        printf("Could not open input.txt!\n");
        exit(1);
    }

    fscanf(fp, "%d", &cntData);
    int pos = 0;
    for (int i = 0; i < cntData; i++) {
        fscanf(fp, "%s %s", compareWord, word);
        /* Call Function*/
        printf("%d\n", subStance(matrix, compareWord, word));
    }

    return 0;
}

int subStance(int matrix[][100], char compareWord[100], char word[100]){
    int wordLen = strlen(word);
    int compareWordLen = strlen(compareWord);

    if (compareWord[0] == word[0]) {
        matrix[0][0] = 1;
    }
    else {
        matrix[0][0] = 0;
    }

    for (int i = 0; i < wordLen; i++) {
        for (int j = 1; j < compareWordLen; j++) {
            matrix[i][j] = matrix[i][j - 1];
            if (word[i] == compareWord[j]) {
                if (i == 0) {
                matrix[i][j] += 1;
                }
                else {
                matrix[i][j] += matrix[i - 1][j - 1];
                }
            }
        }
    }

    int cnt = matrix[wordLen - 1][compareWordLen - 1];

    return cnt;
}