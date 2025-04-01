import sys
input = sys.stdin.readline

T = int(input())


for i in range(1, T + 1):  # i를 1부터 시작하도록 설정
    a, b = map(int, input().split())
    print(f"Case #{i}: {a + b}")  # f-string을 사용해 i 값을 출력