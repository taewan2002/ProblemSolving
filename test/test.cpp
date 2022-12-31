#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<map>
using namespace std;

#define INF 987654321

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int N, M;
	cin >> N >> M;

	int arr[101][101];
	// arr테이블 초기화
	for(int i=1; i<=N; i++){
		for(int j=1; j<=N; j++){
			arr[i][j] = INF;
		}
	}

	// 그래프 입력
	int from, to, weight;
	for(int i=0; i<M; i++){
		cin >> from >> to >> weight;
		if(arr[from][to] > weight){
			arr[from][to] = weight;
		}
	}

	// floyd-warshall
	for(int i=1; i<=N; i++){ // i vertex를 거치는 경우
		for(int j=1; j<=N; j++){ // 시작 vertex
			for(int k=1; k<=N; k++){ // 도착 vertex
				if(arr[j][i] != INF && arr[i][k] != INF)
					arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k]);
			}
		}
	}

	// 출력
	for(int i=1; i<=N; i++){
		for(int j=1; j<=N; j++){
			if(i==j || arr[i][j] == INF){
				cout << 0 << " ";
			}
			else{
				cout << arr[i][j] << " ";
			}
		}
		cout << endl;
	}

    return 0;
}