#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int N, tmp, total;
	cin >> N >> total;
	vector<int> arr;
	while(N--){
		cin >> tmp;
		arr.push_back(tmp);
	}
	sort(arr.begin(), arr.end()); // 1 2 3 5 7 9 10 11 12

	int cnt=0, sum=0, lo=0, hi = arr.size()-1;
	while(lo<hi){
		sum = arr[lo] + arr[hi];
		if(sum > total) hi--;
		else if(sum < total) lo++;
		else{
			cnt++;
			hi--;
			lo++;
		}
	}
	cout << cnt << endl;
}