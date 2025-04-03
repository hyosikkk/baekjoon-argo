a, b = map(str, input().split())  

# 숫자를 뒤집어서 정수로 변환
rev_a = int(a[::-1])  
rev_b = int(b[::-1])  

# 크기 비교 후 출력
print(max(rev_a, rev_b)) 