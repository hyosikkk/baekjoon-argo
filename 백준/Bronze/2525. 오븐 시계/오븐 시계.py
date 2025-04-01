H, M = map(int, input().split())
cook_time = int(input())  # 요리 시간 입력

# cook_time만큼 시간을 더한 후 계산
M += cook_time

# 분(M)이 60 이상이면 시간(H)을 1씩 증가시키고, 분(M)은 60을 초과하지 않도록 조정
while M >= 60:
    M -= 60
    H += 1
    if H == 24:  # 시간이 24시가 되면 0시로 되돌려야 함
        H = 0

print(H, M)