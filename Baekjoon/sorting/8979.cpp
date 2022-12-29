#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;

int N, K;
int gold[1001];
int silver[1001];
int bronze[1001];
int res = 0;

int main() {
	ios_base::sync_with_stdio(false); // c++ 만의 독립버퍼로 시간이 빨라진다.
    cin.tie(nullptr); // cin cout가 서로 묶여있다... 그것을 풀어줌(?)

	//입력
    cin >> N >> K;
    for (int i = 0; i < N; i++) {
        int index;
        cin >> index;
        cin >> gold[index] >> silver[index] >> bronze[index];
    }
 
    //1번 국가부터 N번 국가까지 K번 국가보다 더 잘한 국가일 경우 res++
    for (int i = 1; i <= N; i++) {
        if (gold[i] > gold[K]) {
            res++;
        }
        else if (gold[i] == gold[K]) {
            if (silver[i] > silver[K]) {
                res++;
            }
            else if (silver[i] == silver[K]) {
                if (bronze[i] > bronze[K]) {
                    res++;
                }
            }
        }
    }
 
    //출력
    cout << res + 1;
    return 0;
}