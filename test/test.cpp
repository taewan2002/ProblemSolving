#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

void insertion_sort(vector<int> &arr, int K){
	int N = arr.size();
	int cnt = 0;
	for(int i=1; i<N; i++){
		int loc = i-1;
		int newItem = arr[i];
		while(0 <= loc && newItem < arr[loc]){
			arr[loc+1] = arr[loc];
			cnt++;
			if(cnt == K){
				cout << arr[loc] << endl;
				return;
			}
			loc--;
		}
		if(loc+1 != i){
			arr[loc+1] = newItem;
			cnt++;
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
	insertion_sort(arr, K);
}