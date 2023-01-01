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
	
	
	int N, M;
	cin >> N >> M;

	string s[50];
	int cnt=0;
	for(int i=0; i<N; i++) cin >> s[i];
	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			if(s[i][j] == '-') if(j==M-1 || s[i][j+1] == '|') cnt++;
			if(s[i][j] == '|') if(i==N-1 || s[i+1][j] == '-') cnt++;
		}
	}
	cout << cnt << endl;
	
    return 0;
}