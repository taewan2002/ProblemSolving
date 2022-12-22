#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int N, M, cnt=0, a;
	vector<int> arr;

	cin >> N >> M;
	for(int i=0; i<N; i++){
		cin >> a;
		arr.push_back(a);
	}
	int left=0, right=0, total=0;
	while(left <= right && right <= N){
		if(total > M){
			total -= arr[left];
			left++;
		}
		else if(total < M){
			total += arr[right];
			right++;
		}
		else if(total == M){
			cnt++;
			total += arr[right];
			right++;
		}
	}
	cout << cnt << endl;
}
