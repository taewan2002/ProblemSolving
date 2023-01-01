#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<map>
#include<queue>
using namespace std;

#define INF 987654321
int F, S, G, U, D;
int path[1000001];
bool visited[1000001];
vector<int> arr;
queue<int> q;

void BFS(int v){
	visited[v] = true;
	q.push(v);

	while(!q.empty()){
		v = q.front();
		q.pop();

		for(int i=0; i<2; i++){
			int nv = v + arr[i];

			if(0 < nv && nv <= F){
				if(!visited[nv]){
					visited[nv] = true;
					q.push(nv);
					path[nv] = path[v] + 1;
				}
			}
		}
	}
}



int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)
	
	
	cin >> F >> S >> G >> U >> D;

	arr.push_back(U);
	arr.push_back(D * -1);

	BFS(S);

	if(visited[G]){
		cout << path[G] << endl;
	}
	else{
		cout << "use the stairs" << endl;
	}

    return 0;
}