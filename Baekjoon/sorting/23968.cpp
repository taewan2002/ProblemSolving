#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

void bubble_sort(vector<int> &arr, int K){
	int N = arr.size();
	int lo=0, hi=N-1, cnt=0;
	while(lo < hi){
		if(arr[lo] > arr[lo+1]){
			swap(arr[lo], arr[lo+1]);
			cnt++;
			if(cnt == K){
				cout << arr[lo] << " " << arr[lo+1] << endl;
				return;
			}
		}
		lo++;
		if(lo == hi){
			lo = 0;
			hi--;
		}
	}
	cout << -1 << endl;
}

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)111111

	int N, K;
	cin >> N >> K;
	vector<int> arr(N);
	for(int i=0; i<N; i++){
		cin >> arr[i];
	}

	bubble_sort(arr, K);
}