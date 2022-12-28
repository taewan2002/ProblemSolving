#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int N, A, B, tmp;
	cin >> N;
	while(N--){
		vector<int> arr1, arr2;
		cin >> A >> B; // 각 배열의 크기
		for(int i=0; i<A; i++){
			cin >> tmp;
			arr1.push_back(tmp);
		}
		for(int i=0; i<B; i++){
			cin >> tmp;
			arr2.push_back(tmp);
		}
		sort(arr1.begin(), arr1.end()); // 정렬, [1, 1, 3, 7, 8];
		sort(arr2.begin(), arr2.end()); // [1, 3 ,6];
		int p1=0, total=0;
		for(int i=0; i<arr1.size(); i++){
			while((p1<B) && (arr1[i] > arr2[p1])){
				p1++;
			}
			total += p1;
		}
		cout << total << endl;
	}
}