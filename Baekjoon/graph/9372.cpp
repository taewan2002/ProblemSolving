#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<map>
#include<queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)
	
	
	int N, a, b;
	cin >> N;
	while(N--){
		cin >> a >> b;
		for(int i=0; i<b; i++){
			int tmp1, tmp2;
			cin >> tmp1 >> tmp2;
		}
		cout << a-1 << endl;
	}
    return 0;
}