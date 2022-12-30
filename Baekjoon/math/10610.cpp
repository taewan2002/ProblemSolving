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

	string tmp;
	long long total=0;
	
    cin >> tmp;
	// 역순으로 정렬 ex) 88755420
	sort(tmp.begin(), tmp.end(), greater<>());
	if(tmp[tmp.length()-1] != '0')
		cout << -1 << endl; // 마지막 자리가 0이 아닐 수 없음
	else{
		// 각 자리 수의 합이 3의 배수여야 함?
		for(int i=0; i<tmp.length()-1; i++){
			total += tmp[i] - '0';
		}
		if(total % 3 == 0){
			cout << tmp << endl;
		}
		else{
			cout << -1 << endl;
		}
	}
    return 0;
}