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

	int N;
	cin >> N;

	// 배열 동적 할당
	int **graph = new int*[N];
	for(int i=0; i < N; i++){
		graph[i] = new int[N];
	}

	// 그래프 입력
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			cin >> graph[i][j];
		}
	}

	// floyd-warshall
	// i -> j 로 가는길이 없어도
	// k를 지나갈 수 있으면 갈 수 있음.
	for(int k=0; k<N; k++){
		for(int i=0; i<N; i++){
			for(int j=0; j<N; j++){
				if(graph[i][k] && graph[k][j])
					graph[i][j] = 1;
			}
		}
	}

	// 출력
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			cout << graph[i][j] << " ";
		}
		cout << endl;
	}

	// 자원 반환
	for(int i=0; i<N; i++){
		delete[] graph[i];
	}
	delete[] graph;


    return 0;
}