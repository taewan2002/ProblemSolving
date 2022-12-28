#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int N, tmp, M;
	cin >> N >> M;
	int arr1[N];
	int arr2[M]; // 2번째 배열 생성
	for (int i=0;i<N;i++) {
        cin >> arr1[i];
    }
    for (int i=0;i<M;i++) {
        cin >> arr2[i];
    }
	int p1=0, p2=0;
	while(p1+p2 < N+M){
		if(p1==N){
			cout << arr2[p2] << " "; 
			p2++;
		}
		else if(p2==M){
			cout << arr1[p1] << " "; 
			p1++;
		}
		else{
			if(arr1[p1] < arr2[p2]){
				cout << arr1[p1] << " "; 
				p1++;
			}
			else{
				cout << arr2[p2] << " "; 
				p2++;
			}
		}
		
	}
}