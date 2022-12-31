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

	string str;
    cin >> str;

	int total=0;
	string num;
	bool isMinus = false;

	for(int i=0; i<=str.size(); i++){
		if(str[i]=='-'||str[i]=='+'||i == str.size()){
			if(isMinus){
				total -= stoi(num);
				num.clear();
			}
			else{
				total += stoi(num);
				num.clear();
			}
		}
		else{
			num += str[i];
		}
		if(str[i] == '-'){
			isMinus = true;
		}
	}

	cout << total << endl;
 

    return 0;
}