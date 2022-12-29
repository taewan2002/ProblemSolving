#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int N;

    cin >> N;
	vector<int> arr;
	for(int i=0; i<N; i++){
		int temp;
		cin >> temp;
		arr.push_back(temp);
	}

	sort(arr.begin(), arr.end());

	cout << arr[(N-1)/2] << endl;
    
    return 0;
}