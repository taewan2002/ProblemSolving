#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int N, a;
vector<int> arr;

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> a;
		arr.push_back(a); // 일단 다 집어 넣는다.
	}
	sort(arr.begin(), arr.end()); // 정렬
	arr.erase(unique(arr.begin(),arr.end()), arr.end()); 
	// unique 함수는 중복 제거하며 앞에서부터 채워나간다, 백터 배열의 나머지 자리엔 기존 원소 존재
	// 따라서 지워준다.
	for(int i=0; i<arr.size(); i++){
		cout << arr[i] << " ";
	}
}