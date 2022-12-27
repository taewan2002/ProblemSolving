#include<iostream>
#include<algorithm>
#include<vector>
#include <tuple>
using namespace std;


int fibo(int n){
	if(n==0) return 0;
	if(n==1) return 1;
	return fibo(n-1) + fibo(n-2);
}

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int n;
	cin >> n;
	// n번째 피보나치 수를 출력함
	cout << fibo(n) << endl;

    
    return 0;
}