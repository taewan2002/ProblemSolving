#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<set>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int N;
    cin >> N;

	int K;
	while(N--){
		cin >> K;
		char order;
		int num;
		multiset<int> ms;
		while(K--){
			cin >> order;
			if(order == 'I'){
				cin >> num;
				ms.insert(num);
			}
			else if(order == 'D'){
				cin >> num;
				if(ms.empty()) continue;
				if(num == 1) ms.erase(--ms.end());
				else if(num == -1) ms.erase(ms.begin());
			}
		}
		if(ms.empty()) cout << "EMPTY" << endl;
		else cout << *(--ms.end()) << " " << *ms.begin() << endl;
	}

    return 0;
}