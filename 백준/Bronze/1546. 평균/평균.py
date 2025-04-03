import sys
input = sys.stdin.readline


#gpt 코드
n = int(input())  # 과목 개수
score = list(map(int, input().split()))  # 원래 점수 리스트

M = max(score)  # 최댓값 찾기
new_score = [(s / M) * 100 for s in score]  # 점수 변환

avg = sum(new_score) / len(new_score)  # 평균 계산
print(avg)