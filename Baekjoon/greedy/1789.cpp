#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;

// long long이 int보다 빠르다.. 이유는 모르겠다
// long long은 64비트, int는 32비트

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	long long N;
    cin >> N;
	
	long long total=0, num=1, sum=0;
	while(1){
		sum += num;
		if(sum > N) break;
		num++;
		total++;
	}
	cout << total << endl;
    return 0;
}