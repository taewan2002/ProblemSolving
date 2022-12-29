#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<map>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	long long N;
	long arr[90];
	
    cin >> N;
	arr[0] = 0;
	arr[1] = 1;
	arr[2] = 1;
	for(int i=3; i<=N; i++){
		arr[i] = arr[i-1] + arr[i-2];
	}
	
	cout << arr[N] << endl;
	
    return 0;
}