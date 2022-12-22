#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int N, cnt=0;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	cin >> N;
	// 이렇게 풀면 시간초과 남..
	// for(int i=1; i<(N/2 +2); i++){
	// 	int total=0;
	// 	for(int k=i; k<(N/2 +2); k++){
	// 		total += k;
	// 		if(total == N) cnt++;
	// 	}
	// }
	int left=1, right=1, total=0;
	while(left <= right && right <= N+1){
		if(total > N){
			total -= left;
			left++;
		}
		else if(total < N){
			total += right;
			right++;
		}
		else if(total == N){
			cnt++;
			total += right;
			right++;
		}
	}
	cout << cnt << endl;
}
