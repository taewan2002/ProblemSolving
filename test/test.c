// 문제
// 양의 정수 n과 k가 주어졌을 때, n = p * q이고, p ≤ q, |q-k*p| ≤ 105를 만족하는 소수 p와 q를 찾는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 n과 k가 주어진다. (1 < n < 10^120, 1 < k < 10^8)

// 출력
// 첫째 줄에 문제의 조건을 만족하는 소수 p와 q를 "p * q"형태로 출력한다.


#include <stdio.h>

int main(){
    int n, k;
    scanf("%d %d", &n, &k);
    int p = 0;
    int q = 0;
    int i = 0;
    int j = 0;
    int flag = 0;
    for(i = 2; i < n; i++){
        if(n % i == 0){
            p = i;
            q = n / i;
            if(q - k * p <= 100000 && q - k * p >= -100000){
                flag = 1;
                break;
            }
        }
    }
    if(flag == 1){
        printf("%d * %d", p, q);
    }
    else{
        printf("No Solution");
    }
    return 0;
}