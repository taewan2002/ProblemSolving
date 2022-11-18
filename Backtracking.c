#include <stdio.h>
#define size 6
    
int K = 52; // 목표한 숫자
int w[size] = {2, 10, 13, 17, 22, 42};
char include[size]; // w 집합의 원소 중 경로에 포함되는 지 표시('y' or 'n')
void printSubset(){
    for(int i = 0; i < size; i++)
        if(include[i]!='n')
            printf("%d ",w[i]);
    printf("\n");
}

// 검사할 노드의 하위 노드로 검색할 계속할 지 결정하는 함수
int promising (int i, int weight, int total){
    // weight+total >= K : 현재까지의 노드의 합이 목표한 숫자보다 작은지 검사
    // weight == K : 현재까지의 노드의 합이 목표한 숫자와 같으면 계속 검색
    // weight+w[i+1] == K : 현재까지의 노드의 합에 다음 노드를 더했을 때 목표한 숫자와 같으면 계속 검색
    return (weight+total >= K) && (weight == K || weight+w[i+1] <= K);
}

/* sum_of_subsets 알고리즘을 수행하는 함수
*	i: 집합 w의 인덱스
*	weight: 이동한 가지들의 가중치를 더한다 
*	total: 가지치기에 활용하기위해 집합 w의 모든 원소의 합을 저장
*/

void sum_of_subsets(int i, int weight, int total){
    if(promising(i, weight, total)){
        if(weight == K){ // 현재까지의 노드의 합이 목표한 숫자와 같으면
            printSubset(); // 경로 출력
        }else{
            include[i+1] = 'y'; // 다음 노드를 경로에 포함
            sum_of_subsets(i+1, weight+w[i+1], total-w[i+1]); // 다음 노드로 이동
            include[i+1] = 'n'; // 다음 노드를 경로에 포함하지 않음
            sum_of_subsets(i+1, weight, total-w[i+1]); // 다음 노드로 이동
        }
    }
}


int main() {
    //알고리즘 연산을 위해 필요한 값 초기화
    int total = 0; // total: w 집합 모든 수의 합
    for(int i=0; i<size; i++){
        total += w[i];
        include[i] = 'n';
    }
    //total = 110
    sum_of_subsets(-1, 0, total);
    
    return 0;
}
        