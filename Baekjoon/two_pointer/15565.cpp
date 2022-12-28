#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdlib> // abs가 들어 있네요~
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)111111

	
	int N, K, tmp;
	cin >> N >> K; // N을 입력받는다.
	vector<int> arr;
	for(int i=0; i<N; i++){
		// 1이면 1을 입력, 2면 0을 입력
		// ex) [1, 0, 0, 0, 1, 0, 1, 0, 0 ,1]
		// k=3 -> 누적합이 3이 되는 가장 짧은 배열
		// 1. [1, 0, 0, 0, 1, 0, 1]
		// 2. [1, 0, 1, 0, 0, 1]
		cin >> tmp;
		if(tmp == 2) arr.push_back(0);
		else arr.push_back(tmp);
	}
	arr.push_back(0); // 마지막칸에 1이 있을 경우 까지 대비


	int min_size=1000000, tmp_min;
	int lo=0, hi=0, total = 0;
	while(hi<arr.size()){
		if(total < K){
			total += arr[hi];
			hi++;
		}
		else{
			tmp_min = hi - lo;
			if(tmp_min < min_size) min_size = tmp_min;
			total -= arr[lo];
			lo++;
			while(arr[lo] != 1){ // lo 포인터가 다음 1을 가르킬때 까지 올림
				lo++;
			}
		}
	}
	if(min_size == 1000000) cout << -1 << endl;
	else cout << min_size << endl;
}