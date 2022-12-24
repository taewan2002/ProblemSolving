#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)111111

	vector<int> arr;
	int N;
	cin >> N; // N을 입력받는다.
	vector<int> check(N+1, 1); // N+1 칸을 1로 체워라!
	
	// N 보다 작은 소수를 구한다.. 에라토스테네스의 체
	for(int i=2; i*i<=N; i++){
		if(check[i] == 1){
			for(int j=i+i; j<=N; j+=i)
				check[j] = 0; // 각 수의 배수를 전부 0으로 바꾼다.
		}
	}
	// 각 수의 배수가 아닌 수를 arr에 저장, 소수
	for(int i=2; i<=N; i++){
		if(check[i] == 1){
			arr.push_back(i);
		}
	}
	
	int total=0, lo=0, hi=0, ans=0;
	while(1){
		if(total > N){ // 총합이 목표값을 넘어버리면 첫 번째 포인터를 이동
			total -= arr[lo];
			lo++;
		}
		else if(total < N){ // 총합이 목표값보다 작다면 계속 진행
			if(hi >= arr.size()) break; // 두번째 포인터가 배열 밖으로 나가면 종료
			total += arr[hi];
			hi++;
		}
		else{ // 총 합이 같다면 ans++ 후 이어서 진행
			ans++;
			if(hi >= arr.size()) break; // 두번째 포인터가 배열 밖으로 나가면 종료
			total += arr[hi];
			hi++;
		}
	}
	cout << ans << endl;
}