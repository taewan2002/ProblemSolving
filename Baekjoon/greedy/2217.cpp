#include<iostream>
#include<algorithm>
#include<vector>
#include <tuple>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	vector<int> arr;

	int N,tmp;
	cin >> N;
	for(int i=0; i<N; i++){
		cin >> tmp;
		arr.push_back(tmp);
	}
	sort(arr.begin(), arr.end(), greater<int>()); // 내림차순 정렬
	int sum=0, max = 0;
	for(int i=0; i<arr.size(); i++){
		sum = arr[i] * (i+1);
		if(sum > max){
			max = sum;
		}
	}
	cout << max << endl;

    return 0;
}