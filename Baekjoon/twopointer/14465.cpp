#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)111111

	
	int N, K, B, tmp;
	cin >> N >> K >> B; // N을 입력받는다.
	vector<int> arr(N+1, 0); // 0인 배열을 만든다.
	for(int i=0; i<B; i++){
		cin >> tmp;
		arr[tmp] = 1; // 고장난 신호등을 1로 표시한다.
	}
	// 6칸을 검사해서 1의 min값 출력? 굿
	int lo=1, hi=1, total = 0, min=N;
	while(hi < N+1){
		total += arr[hi];
		hi++;
		if(hi - lo == K){
			if(min>total) min = total;
			total -= arr[lo];
			lo++;
		}
	}
	cout << min << endl;
}