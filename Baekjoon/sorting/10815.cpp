#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int N, a;
vector<int> arr;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	cin >> N;
	while(N--){
		cin >> a;
		arr.push_back(a); // 일단 다 집어 넣는다.
	}
	sort(arr.begin(), arr.end()); // search 하기 위해 정렬한다.
	cin >> N;
	while(N--){
		cin >> a;
		cout << binary_search(arr.begin(), arr.end(), a) << " ";
	}
}