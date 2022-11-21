#include<stdio.h>
#include<stdlib.h>
// can not solve this problem

int main(){
    long long a, b, cnt;
    while(1){
        cnt = 0;
        scanf("%lld %lld", &a, &b);
        if(a==0 && b==0) break;
        long long *dp = (long long*)malloc(sizeof(long long)*b);
        dp[0] = 1;
        dp[1] = 2;
        int n = 2;
        while(1){
            dp[n] = (dp[n-1] + dp[n-2]);
            if(dp[n] >= b) break;
            n++;
        }
        for(int i=0; i<n; i++){
            // printf("dp[%d] = %d\n", i, dp[i]);
            if(dp[i] >= a && dp[i] <= b) cnt++;
        }
        printf("%lld\n", cnt);
    }
    return 0;
}