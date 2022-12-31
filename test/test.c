#include <stdio.h>

int main(){
    
    int n;
    int cnt=0;
    for(int i=1; i<=n; i++){
        if(n%i == 0){
            cnt++;
        }
    }
    if(cnt == 2){
        printf("소수입니다\n");
    }
    else{
        printf("소수가 아닙니다\n");
    }
    return 0;
}         