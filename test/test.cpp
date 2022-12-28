#include<iostream>
#include<algorithm>
#include<vector>
#include <tuple>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int N, K, cnt=0;
	cin >> N >> K;

	vector<int> arr(N+1);
	for(int i=2; i<=N; i++){
		for(int k=i; k<=N; k+=i){
			if(arr[k] == 0){
				arr[k] = 1;
				cnt++;
				if(cnt == K){
					cout << k << endl;
					exit(0);
				}
			}
		}
	}
    return 0;
}