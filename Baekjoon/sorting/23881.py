def selection_sort(arr, k): 
    cnt = 0
    for i in range(n-1, 0 , -1):
        max_idx = 0
        for j in range(1, i+1): 
            if arr[max_idx] < arr[j]: 
                max_idx = j
        if max_idx != i:
            cnt += 1
            arr[i], arr[max_idx] = arr[max_idx], arr[i] 
        if cnt == k:
            print(arr[max_idx], arr[i])
            return
    print(-1)
    

n, k = map(int, input().split())
select_list = list(map(int, input().split()))

selection_sort(select_list, k)