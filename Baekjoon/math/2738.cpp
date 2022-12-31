#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<map>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	int row, col, tmp;
	cin >> row >> col;

	// 2차원 배열 동적할당
	int **arr = new int*[row];
	for(int i=0; i<row; i++){
		arr[i] = new int[col];
	}

	// 첫 번째 행렬 입력받기
	for(int k=0; k<row; k++){
		for(int i=0; i<col; i++){
			cin >> arr[k][i];
		}
	}

	// 두 번째 행렬 입력받기
	for(int k=0; k<row; k++){
		for(int i=0; i<col; i++){
			cin >> tmp;
			arr[k][i] += tmp;
		}
	}

	// 출력
	for(int k=0; k<row; k++){
		for(int i=0; i<col; i++){
			cout << arr[k][i] << " ";
		}
		cout << "\n";
	}

	// 할당 해제
	for(int i=0; i<row; i++){
		delete[] arr[i];
	}
	delete[] arr;

    return 0;
}