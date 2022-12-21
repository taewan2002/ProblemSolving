#include<iostream>
using namespace std;

int N, sum, sum_2;

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		sum += a;
		sum_2 += (a / 2); // 2를 붓는 횟수

	}
	if (sum % 3 == 0) {
		// 2로 성장 시킬 수 있는 횟수가 총합의 1/3 이상이면 된다.
		if (sum_2 >= (sum / 3)) {
			cout << "YES\n";
			return 0;
		}
		else {
			cout << "NO\n";
			return 0;
		}
	}
	else {
		// 3의 배수가 아니면 무조건 안된다.
		cout << "NO\n";
	}
}
