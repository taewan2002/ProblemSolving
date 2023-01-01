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
int N, M, from, to, x, y;
int visited[101];
int arr[101][101];
queue<int> q;

void BFS(int v){
	q.push(v);

	while(!q.empty()){
		v = q.front();
		q.pop();

		for(int i=1; i<=N; i++){
			if(arr[v][i]!=0 && !visited[i]){
				q.push(i);
				visited[i] = visited[v] + 1;
			}
		}
	}
}



int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)
	
	
	cin >> N;
	cin >> from >> to;
	cin >> M;
	for(int i=0; i<M; i++){
		cin >> x >> y;
		arr[x][y] = 1;
		arr[y][x] = 1;
	}

	BFS(from);

	if(visited[to]){
		cout << visited[to] << endl;
	}
	else{
		cout << "-1" << endl;
	}

    return 0;
}