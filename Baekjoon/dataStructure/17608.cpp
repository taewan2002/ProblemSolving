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

	long long N, tmp;
	long long arr[100000];
	
    cin >> N;
	for(int i=0; i<N; i++){
		cin >> tmp;
		arr[i] = tmp;
	}
	long long total=1;
	long long max_num = arr[N-1];
	for(int i=N-1; i>=0; i--){
		if(arr[i] > max_num){
			total++;
			max_num = arr[i];
		}
	}
	cout << total << endl;
	
    return 0;
}