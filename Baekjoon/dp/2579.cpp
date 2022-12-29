#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<map>
using namespace std;

long long dp[301];
int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	long long N, tmp;
	vector<long long> arr;
	
    cin >> N;
	for(int i=0; i<N; i++){
		cin >> tmp;
		arr.push_back(tmp);
	}
	
	dp[0] = arr[0];
	dp[1] = arr[0] + arr[1];
	dp[2] = max(arr[0] + arr[2], arr[1] + arr[2]);

	for(int i=3; i<N; i++){
		dp[i] = max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2]);
	}

	cout << dp[N-1] << endl;

	//`dp[0] = 10
	// dp[1] = 10 + 20 = 30
	// dp[2] = 10 + 15 vs 20 + 15 = 35
	// dp[3] = 25 + arr[2] + dp[3-3] vs 25 + dp[3-2]
	// dp[4] = 10 + arr[3] + dp[4-3] vs 10 + dp[4-2]
	
    return 0;
}