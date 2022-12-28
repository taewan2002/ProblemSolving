#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;


bool isPrime(int num) {
    if(num < 2) return false;

	// 2부터 num의 제곱근까지 나눠보면 된다.
	// 시간복잡도는 O(sqrt(n))
    for(int i = 2 ; i <= sqrt(num) ; i++) {
        if(num % i == 0) return false;
    }

    return true;
}

bool isPalindrome(string str) {
    string front, back;
    
    front = str;
    reverse(str.begin(), str.end());
    back = str;

    if(front == back) return true;
    else return false;
}

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int a, b;
	cin >> a >> b;

    for(int i = a ; i <= 10000000 ; i++) {
        if(i > b) break;
        if(isPalindrome(to_string(i)) && isPrime(i)) {
            cout << i << endl;
        }
    }

    cout << -1 << endl;

    return 0;
}