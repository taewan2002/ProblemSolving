#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)111111

	int N, tmp;
	vector<int> arr;
	cin >> N;
	for(int i=0; i<N; i++){
		cin >> tmp;
		arr.push_back(tmp);
	}
	sort(arr.begin(), arr.end());

	// 자꾸 시간 초과나는데 어떡해...?
	int lo=0, hi=N-1, total, cnt=0;
	for(int i=0; i<N; i++){
		total = arr[i]; // 두 수의 합이 돼야 할 수
		while(lo < hi){
			// total을 두수의 합으로 만들 수 있으면 cnt를 올린다.
			if (lo == i){
				lo++;
				continue;
			}
			else if(hi == i){
				hi--;
				continue;
			}
			if(arr[lo] + arr[hi] == total){
				cnt++;
				break;
			}
			else if(arr[lo] + arr[hi] > total){
				hi--;
			}
			else{
				lo++;
			}
		}
		lo=0;
		hi = N-1;
	}
	cout << cnt << endl;
}