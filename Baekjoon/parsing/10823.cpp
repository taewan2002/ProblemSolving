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

	string tmp, s;
	int total = 0;
	while(getline(cin, s)){
		for(int i=0; i < s.length(); i++){
			if(s[i] != ','){
				tmp += s[i]; // 숫자만 쭉 더한다
			}
			else{
				total += stoi(tmp);
				tmp.clear();
			}
		}
	}
	total += stoi(tmp);
	cout << total << endl;
    return 0;
}