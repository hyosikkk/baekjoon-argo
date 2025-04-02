# gpt로 수정한 코드
numbers = []
for _ in range(10):
    num = int(input())
    numbers.append(num)

# 42로 나눈 나머지를 저장
numbers_mod = [num % 42 for num in numbers]

# 중복 제거 (서로 다른 나머지 개수)
count = len(set(numbers_mod))

print(count)  # 서로 다른 나머지의 개수 출력