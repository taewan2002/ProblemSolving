#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<map>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	long long N, K;
    cin >> N;
	while(N--){
		vector<long long> arr;
		cin >> K;
		if(K < 4) cout << 1 << endl;
		else{
			arr.push_back(1);
			arr.push_back(1);
			arr.push_back(1);
			for(int i=3; i<K; i++){
				arr.push_back(arr[i-3] + arr[i-2]);
			}
			cout << arr[K-1] << endl;
		}
	}
    return 0;
}