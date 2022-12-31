#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct data{
    int x;
    int y;
};
// ccw
int ccw(double x1, double y1, double x2, double y2, double x3, double y3){
    double temp = x1*y2 + x2*y3 + x3*y1;
    temp = temp - y1*x2 - y2*x3 - y3*x1;
    if(temp > 0) return 1; //ccw
    else if(temp < 0) return -1; //cw
    else return 0; //collinear
}
// distance
double distance(double x1, double y1, double x2, double y2){
    double d;
    d = sqrt(pow(x2-x1,2) + pow(y2-y1,2));
    return d;
}

struct data dat[6000];

int main(){
    int hull[6000];
    int count=0;
    int n;
    double d=0;
    float total;
    scanf("%d",&n);
    for(int k=0; k<n; k++){
        scanf("%d %d", &dat[k].x, &dat[k].y);//read data
    }
    //gift wrapping algorithm
    int min_index = 0;
    int min_x = 100000;
    int min_y = 100000;
    for(int i=0; i<n; i++){
        if(dat[i].x < min_x){
            min_x = dat[i].x;
            min_y = dat[i].y;
            min_index = i;
        }
        else if(dat[i].x == min_x){
            if(dat[i].y < min_y){
                min_x = dat[i].x;
                min_y = dat[i].y;
                min_index = i;
            }
        }
    }
    
    hull[0] = min_index;
    count = 1;
    int next = 0;
    while(1){
        int temp = 0;
        for(int j=0; j<n; j++){
            if(j == hull[count-1]) continue;
            int ccw_result = ccw(dat[hull[count-1]].x, dat[hull[count-1]].y, dat[next].x, dat[next].y, dat[j].x, dat[j].y);
            if(ccw_result == -1){
                next = j;
            }
            else if(ccw_result == 0){
                if(distance(dat[hull[count-1]].x, dat[hull[count-1]].y, dat[next].x, dat[next].y) < distance(dat[hull[count-1]].x, dat[hull[count-1]].y, dat[j].x, dat[j].y)){
                    next = j;
                }
            }
        }
        if(next == hull[0]) break;
        hull[count] = next;
        count++;
    }
    
    for(int i=0; i<count-1; i++){
        d+=distance(dat[hull[i]].x,dat[hull[i]].y,dat[hull[i+1]].x,dat[hull[i+1]].y);
    }
    d+=distance(dat[hull[0]].x,dat[hull[0]].y,dat[hull[count-1]].x,dat[hull[count-1]].y);
    
    printf("%.2lf", d);
    return 0;
}