#include <cstdio>
#include <cstring>
#include <cmath>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

struct Point
{
    double x, y;

    Point(double x = 0, double y = 0):
        x(x), y(y) {}
    void read() {
        scanf("%lf%lf", &x, &y);
    }
} p[105];

int n;
int dir[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

double Distance(Point a, Point b)
{
    return sqrt((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y));
}
double getVal(Point ini)
{
    double ret = 0;
    for(int i = 0; i < n; ++i) {
        ret += Distance(ini, p[i]);
    }
    return ret;
}
int main()
{
    while(scanf("%d", &n) != EOF)
    {
        for(int i = 0; i < n; ++i)
        {
            p[i].read();
        }
        Point pre, cur;
        double res = getVal(pre);
        double step = 100;
        while(step > 0.2)
        {
            bool OK = true;
            while(OK)
            {
                OK = false;
                for(int i = 0; i < 4; ++i)
                {
                    cur.x = pre.x + dir[i][0] * step;
                    cur.y = pre.y + dir[i][1] * step;
                    double ret = getVal(cur);
                    if(ret < res)
                    {
                        res = ret;
                        pre = cur;
                        OK = true;
                    }
                }
            }
            step /= 2.0;
        }
        printf("%d\n", (int)floor(res+0.5));
    }
    return 0;
}