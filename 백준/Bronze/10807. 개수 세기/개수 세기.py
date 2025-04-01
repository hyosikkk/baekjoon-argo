n = int(input())  
arr = list(map(int, input().split()))  
v = int(input())  

count_v = 0  # 카운트 초기화
for num in arr:
    if num == v:
        count_v += 1  # v와 같은 숫자가 나오면 카운트 증가

print(count_v)