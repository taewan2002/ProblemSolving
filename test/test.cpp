#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<map>
#include<queue>
using namespace std;

bool compare(const pair<int, string> &a, const pair<int, string> &b){
	if(a.first == b.first){
		if(a.second.length() < b.second.length()){
			return a.second < b.second;
		}
		else if(a.second.length() > b.second.length()){
			return a.second > b.second;
		}
		else{
			if(a.second < b.second){
				return a.second < b.second;
			}
			else{
				return a.second > b.second;
			}
		}
	}
	return a.first < b.first;
}


int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)
	
	vector<pair<int, string>> blue;
	vector<pair<int, string>> white;

	int N, M, a;
	string b;
	cin >> N >> M;
	int *cnt = new int[N+1];
	for(int i=0; i<N+1; i++){
		cnt[i] = 0;
	}
	while(true){
		cin >> a >> b;
		if(a==0 && b[0]=='0') break;
		if(a%2==0 && cnt[a] < M){
			white.push_back(make_pair(a, b));
			cnt[a]++;
		}
		else if(a%2!=0 && cnt[a]<M){
			blue.push_back(make_pair(a,b));
			cnt[a]++;
		}
	}
	sort(white.begin(), white.end(), compare);
	sort(blue.begin(), blue.end(), compare);

	for(auto it: blue){
		cout << it.first << " " << it.second << endl;
	}
	for(auto it: white){
		cout << it.first << " " << it.second << endl;
	}

	delete[] cnt;
    return 0;
}