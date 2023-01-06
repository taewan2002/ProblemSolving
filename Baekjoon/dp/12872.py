import sys
input = sys.stdin.readline

MOD = int(1e9+7)
N, M, P = map(int, input().split())

# 모든 노래 N개를 사용해야됨
# 같은 노래를 추가하려면 두 노래 사이에 적어도 M개의 노래가 있어야함
# P개의 노래를 플레이리스트로 만들려고함 M <= P
# 1 <= N <= 100
dp = [list([0 for _ in range(P+1)]) for _ in range(P+1)]
dp[0][0] = 1
for i in range(1, P+1):
    for j in range(N+1):
        # i 플레이리스트의 길이
        # j 꼭 포함되어야 하는 노래갯수
        if(j>0):
            dp[i][j] += dp[i-1][j-1] * (N-j+1)
            dp[i][j] %= MOD
        if(j>M):

            dp[i][j] += dp[i-1][j] * (j-M)
            dp[i][j] %= MOD

print(dp[P][N])

# M = 0 6 * 6* 6
# M = 1 6 * 5 * 5
# M = 2 6 * 5 * 4 * 4 * 4

# p = 처음부터 추가한 곡의 갯수
# sel = 이미 플레이 리스트에 한곡 이상 추가 한 수
# dp[p, sel] = (모든노래-이미 추가한 수 + 1) * D(p-1, sel-1) + (sel - M) * D(p-1, sel)(if, sel>M)
