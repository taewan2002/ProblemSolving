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
 
    bool isCpp = false, isJava = false, isError = false;
    string result;
 
    for (int i = 0; i < str.length(); i++){
        // java
        if (isupper(str[i])){ // 대문자 이면서
            if (!i || isCpp){ // 첫글자이거나 cpp 언어가 아닌 경우
                isError = true;
                break;
            }
            // 들어온 문자가 java 언어이므로 이를 cpp 로 바꾸기 위해서
            // '_' 를 추가해주고, str[i] - 'A' + 'a' 는 아스키 코드 연산에 의해서 소문자로 바꾸겠다는 의미다.
            result += '_';
            result += str[i] - 'A' + 'a';
            isJava = true; // 위 과정을 다 거치면 비로소 java 가 되므로 true 로 바꿈
        }
        // cpp
        else if (str[i] == '_'){
            // '_' 가 들어간 경우
            if (!i || isJava || i == str.length() - 1 || str[i + 1] == '_' || isupper(str[i + 1])){ // 첫글자 이거나, 자바이거나, 끝 - 1 이거나(i + 1 번째에 대한 연산 필요), 다음글자에 _가 있거나 (연속된 '_' 가 오는 경우), 다음 문자가 대문자('_' 다음에 대문자가 온다는 뜻) 이거나 하면 오류다
                isError = true;
                break;
            }
            // 소문자로 바꿔서 삽입
            result += str[i + 1] - 'a' + 'A';
            i++;
            isCpp = true; // 위 과정을 다 거치면 비로소 cpp 가 되므로 true 로 변경
        }
        else{
            // 대문자나 '_' 둘다 아닌 경우 (소문자 일때) 는 그냥 삽입
            result += str[i];
        }
    }
    if (isError)
        cout << "Error!\n";
    else
        cout << result << '\n';

    return 0;
}