n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

blue_count = 0
white_count = 0


def makePaper(x, y, n):
    global blue_count, white_count

    check_color = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check_color != graph[i][j]:
                # x, y가 0이나오면 절반으로 쪼갠다.
                check_color = -1
                break

    if check_color == -1:
        n = n // 2
        makePaper(x, y, n)
        makePaper(x + n, y, n)
        makePaper(x, y + n, n)
        makePaper(x + n, y + n, n)
    elif check_color == 1:
        blue_count += 1
    elif check_color == 0:
        white_count += 1


makePaper(0, 0, n)
print(white_count)
print(blue_count)