#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	while(1){
		int N;
		cin >> N;
		if(N == 0) break;
		vector<int> arr(2*N+1, 0);
		int cnt = 0;
		// 에라토스테네스의 체
		for(int i=2; i<=sqrt(2*N+1); i++){
			for(int k=i; k<=2*N+1; k+=i){
				if(arr[k] == 0){
					arr[k] = 1;
				}
			}
		}

		for(int i=N+1; i<=N*2; i++){
			if(arr[i] == 0) cnt++;
		}

		cout << cnt << endl;
	}
    return 0;
}