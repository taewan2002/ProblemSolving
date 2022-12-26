#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)111111

	vector<int> arr;
	int N=5;
	while(N--){
		int tmp;
		cin >> tmp;
		arr.push_back(tmp);
	}
	sort(arr.begin(), arr.end());
	int sum=0;
	for(int i=0; i<arr.size(); i++){
		sum += arr[i];
	}
	cout << sum/arr.size() << endl;
	cout << arr[arr.size()/2] << endl;
}