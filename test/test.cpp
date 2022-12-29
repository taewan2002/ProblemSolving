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

	char s[100];
	
    cin >> s;
	for(int i=0; s[i] != '\0'; i++){
		if(s[i] >= 65 && s[i] <= 90){
			s[i] += 32;
		}
		else{
			s[i] -= 32;
		}
	}
	cout << s << endl;
	
    return 0;
}