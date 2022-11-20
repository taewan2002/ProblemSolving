#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<iostream>
using namespace std;

long long A, B, C;
long long multiply(int n)
{
    long long left, right;
    if (n == 1) return A % C;
    else if (n == 2) return ((A%C) * (A%C)) % C;
    if (n % 2)
    {
        left = multiply(n / 2);
        right = multiply(n / 2 + 1);
    }
    else
    {
        left = multiply(n / 2);
        right = multiply(n / 2);
    }
    return ((left%C) * (right%C)) % C;
}

int arr[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, //1 ~ 25 prime number 
	             43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
				 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
				 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
				 199, 211, 223, 227, 229, 233, 239, 241, 251}; 



int main(){
    // 5, 119, 66
    int e, n, c;
    int p, q;
    int k;
    int d;

    FILE* fb = fopen("input.txt", "r");
    if(fb==NULL){
        printf("Could not open input.txt!\n");
        exit(1);
    }
    
    while (feof(fb) == 0){
        fscanf(fb, "%d %d %d", &e, &n, &c);
        
        // step#1 : find  p and q 
        for(int i=0; i<52; i++){
            for(int j=i; j<53; j++){
                if(arr[i] * arr[j] == n){
                    p = arr[i];
                    q = arr[j];
                }
            }
        }

        // step#2 : find φ(n)
        k = (p-1) * (q-1);

        // step#3 : find d
        int m = 1;
        while(1){
            for(int i=1; i<k; i++){
                if(e * i == m*k+1){
                    d = i;
                    goto point;
                }
            }
            m++;
        }
        point:

        // step#4 : decrypt
        A =  c; // 66
        B = d; // 77
        C = n; // 119
        printf("original message is %lld\n", multiply(B));
    }
	return 0;
}