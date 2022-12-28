# import sys
# input = sys.stdin.readline
 
n = int(input())
str1 = str(input().strip())
 
dic = {}
result = [0, 0]
start = 0
end = 0
 
while start < len(str1) and end < len(str1):
 
    if str1[end] not in dic:
        dic[str1[end]] = 1
    else:
        dic[str1[end]] += 1
 
    # 만약 딕셔너리안에 n개보다 더 많은 알파벳이 들어갔을경우
    # start값을 올려서 n개가 되도록 알파벳을 빼줘야한다.
    if len(dic) > n:
        while start <= end and len(dic) > n:
            if dic[str1[start]] == 1:
                dic.pop(str1[start])
            else:
                dic[str1[start]] -= 1
            start += 1
 
    # 만약 연속된 n개의 문자열이 들어왔을경우
    # result안에 최대 길이가 들어갈 수 있도록 넣어준다.
    if len(dic) <= n:
        # 최대길이로 갱신해주자~
        if result[1] - result[0] < end - start:
            result[0] = start
            result[1] = end
 
    end += 1
 
print(result[1] - result[0] + 1)