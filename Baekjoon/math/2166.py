def ccw(x1, y1, x2, y2, x3, y3):
    val = (x1 * y2) + (x2 * y3) + (x3 * y1) - (y1 * x2) - (y2 * x3) - (y3 * x1)
    return val/2
    


n = int(input())
x_list = []
y_list = []
for i in range(n):
    a, b = map(int, input().split())
    x_list.append(a)
    y_list.append(b)
x_list.append(x_list[0])
y_list.append(y_list[0])

area = 0
for i in range(n):
    area += ccw(x_list[i], y_list[i], x_list[i+1], y_list[i+1], 0, 0)
print(abs(area))