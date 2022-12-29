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

	int N, K;
	string tmp1, tmp2;
    cin >> N;
	while(N--){
		map<string, int> m;
		cin >> K;
		while(K--){
			cin >> tmp1 >> tmp2;
			if(m.find(tmp2) == m.end())
				// 값이 없다면 종류 삽입
				m.insert({tmp2, 1});
			else m[tmp2]++; // 이미 았다면 카운트
		}
		int total=1;
		for(map<string, int>::iterator i=m.begin(); i!=m.end(); i++){
			total *= (i ->second +1);
		}
		cout << total -1 << endl;
	}

    return 0;
}