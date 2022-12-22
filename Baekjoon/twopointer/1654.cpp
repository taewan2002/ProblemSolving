#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int N, tmp, total;
	cin >> N >> total;
	vector<unsigned int> arr; // overflow 방지
	while(N--){
		cin >> tmp;
		arr.push_back(tmp);
	}
	sort(arr.begin(), arr.end()); // max값을 구하기 위해

	unsigned int sum=0, lo=1, hi=arr[arr.size()-1], mid;
	while(lo<hi){
		mid = (lo + hi) / 2 + 1; // 맨첨에 400으로 갯수를 센다
		sum = 0;
		for(int i=0; i<arr.size(); i++){
			sum += (arr[i] / mid); // 총 갯수 확인
		}
		if(sum >= total) lo = mid; // 총 갯수가 원하는 갯수가 되면 정지
		else hi = mid - 1; // 399로 다시 시도
	}
	cout << lo << endl;
}