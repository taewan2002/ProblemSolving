#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)111111

	vector<int> arr;
	int N, K, tmp;
	cin >> N >> K; // N을 입력받는다.

	while(N--){
		cin >> tmp;
		arr.push_back(tmp);
	}
	int lo=0, hi=0, total = 0, max=-1e9;
	while(1){
		total += arr[hi];
		hi++;
		if(hi - lo == K){
			if(total > max) max = total;
			total -= arr[lo];
			lo++;
		}
		if(hi == arr.size()) break;
	}
	cout << max << endl;
}