#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
    int temp, tempti, tempsi; // temporary variable
	int n, r;
	int result[1001];
	int ti[1001], si[10001];

    /* Load File */
    FILE* fp;
    fp = fopen("input.txt", "r");
    if (fp == NULL) { // Check availiable file
        printf("Could not open input.txt!\n");
        exit(1);
    }

    fscanf(fp, "%d", &temp);
    for (int i = 0; i < temp; i++) {
		fscanf(fp, "%d", &n);
		for (int i = 0; i < n; i++) {
			fscanf(fp,"%d %d", &tempti, &tempsi);
			ti[r] = tempti;
			si[r++] = tempsi;

		}

		for (int k = 0; k < n; k++) {
			/* count number */
			result[k] = k;
		}

		/* algorithm */
		for (int i = 1; i < n; i++) {
			for (int j = 0; j < n - i; j++) {
				/* compare two data and sorting small count */
				if (ti[result[j]] * si[result[j + 1]] > ti[result[j + 1]] * si[result[j]]) {
					/* swap the number */
					temp = result[j];
					result[j] = result[j + 1];
					result[j + 1] = temp;
				}
			}
		}

		/* print the data */
		for (int i = 0; i < n; i++)
			printf("%d ", result[i] + 1);
		printf("\n");
	}
    return 0;
}