#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<map>
#include<queue>
using namespace std;

struct cmp {
	bool operator()(pair<int, string> a, pair<int, string> b) {
		if (a.first == b.first)
			return a.second > b.second;
		return a.first <= b.first;
	}
};

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)
	
	int N;
	priority_queue<pair<int, string>, vector<pair<int, string>>, cmp> q;
	string str, tmp;
	cin >> str;
	cin >> N;
	while(N--){
		cin >> tmp;
		int L=0, O=0, V=0, E=0;
		for(auto c:str+tmp){
			switch(c){
				case 'L': L++; break;
				case 'O': O++; break;
				case 'V': V++; break;
				case 'E': E++; break;

			}
		}
		int total = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100;
		q.push({total, tmp});
	}

	cout << q.top().second << endl;
    return 0;
}