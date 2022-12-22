#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int N, tmp, M;
	cin >> N >> M;
	vector<unsigned int> arr; // overflow 방지
	while(N--){
		cin >> tmp;
		arr.push_back(tmp);
	}

	int total=arr[0], lo=0, hi=0, min_value = 100000001;
	while(lo <= hi && hi <= arr.size()){
		if(total >= M) min_value = min(min_value, hi-lo+1); // 원하는 값이거나 더 크면 min_value업데이트
		if(total < M){ // 원하는 값보다 작으면 hi 포인터를 이동하면서 누적합을 구함
			hi++;
			total += arr[hi];
		}
		else if(total >= M){ // 원하는 값보다 크면 lo 포인터를 이동하고 누적합에서 제거
			total -= arr[lo];
			lo++;
		}
	}
	if(min_value == 100000001) cout << "0" << endl;
	else cout << min_value << endl;
}