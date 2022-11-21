#include<stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    int dp[1000001] = {0, 1, 1};
    for(int i=3; i<=n; i++)
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007;
    printf("%d\n", dp[n]);

    return 0;
}