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

	int N;
	string tmp;
	int A, B;
	cin >> N;
	while(N--){
		cin >> tmp;
		for(int i=0; i != ','; i++){
			A = tmp[0] - '0';
			B = tmp[2] - '0'; 
		}
		cout << A + B << endl;
	}
    return 0;
}