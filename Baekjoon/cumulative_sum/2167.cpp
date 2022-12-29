#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;

// long long이 int보다 빠르다.. 이유는 모르겠다
// long long은 64비트, int는 32비트

long long arr[301][301];
int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	long long N, K;
    cin >> N >> K;
	
	for(int i=1; i<=N; i++){
		for (int j=1; j<=K; j++){
			cin >> arr[i][j];
			arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]; // 누적합
		}
	}

	long long M;
	cin >> M;
	for(int i=0; i<M; i++){
		long long x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		cout << arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1] << endl;
	}

    return 0;
}