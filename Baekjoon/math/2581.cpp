#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;

int t=0;
int min_num;
bool isPrime(int num) {
    if(num < 2) return false;

	// 2부터 num의 제곱근까지 나눠보면 된다.
	// 시간복잡도는 O(sqrt(n))
    for(int i = 2 ; i <= sqrt(num) ; i++) {
        if(num % i == 0) return false;
    }
	if (t == 0) {
		min_num = num;
		t++;
	}
    return true;
}

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int a, b;
	cin >> a >> b;
	int cnt = 0;

    for(int i = a ; i <= 10000000 ; i++) {
        if(i > b) break;
        if(isPrime(i)) {
            cnt += i;
        }
    }
	if(cnt != 0) cout << cnt << "\n" << min_num << endl;
	else cout << -1 << endl;

    return 0;
}