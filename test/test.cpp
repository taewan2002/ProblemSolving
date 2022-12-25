#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	// ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    // cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)111111

	
	int N;
	int arr[26];
	char s[100001];

	cin >> N; // N을 입력받는다.
	scanf("%s", s);
	arr[s[0] - 'a'] += 1;

	int cnt=1, ans=1, lo=0;
	// 문자열 길이 만큼 반복한다.
	for(int i=1; s[i] != 0; i++){
		
		// i번째 문자열에 대해 업데이트 한다.
		if(arr[s[i] - 'a'] == 0){
			cnt += 1;
		}
		arr[s[i] - 'a'] += 1;

		// 업데이트 이후 종류가 N개보다 크다면 왼쪽에서 제외
		while(cnt > N){
			arr[s[lo] - 'a'] -= 1;
			if(arr[s[lo] - 'a'] == 0){
				cnt -= 1;
			}
			lo++;
		}

		// 왼쪽에서부터 제거해서 N보다 작아진 시점보다 +1 한 결과값을 구함
		if (i - lo + 1 > ans){
			ans = i - lo + 1;
		}
	}
	cout << ans << endl;
}