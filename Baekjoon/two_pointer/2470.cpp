#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdlib> // abs가 들어 있네요~
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)111111

	
	int N, tmp;
	cin >> N; // N을 입력받는다.
	vector<int> arr;
	for(int i=0; i<N; i++){
		cin >> tmp;
		arr.push_back(tmp);
	}
	// 정렬 한다 으이?
	sort(arr.begin(), arr.end());

	int lo_value, hi_value;
	int lo=0, hi=arr.size()-1, total = 0, abs_value=2000000000; // 20억
	while(lo<hi){
		total = arr[lo] + arr[hi]; // 일단 두 개 더해봐
		if(abs_value > abs(total)){
			abs_value = abs(total);
			lo_value = lo; // 작은 수의 인덱스 저장
			hi_value = hi; // 큰 수의 인덱스 저장
		}
		if(total < 0){ // 작은수를 더 크게
			lo++;
		}
		else{ // 큰 수를 더 작게
			hi--;
		}
	}
	cout << arr[lo_value] << " " << arr[hi_value] << endl;
}