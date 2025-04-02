student = list(range(1, 31))  # 1번부터 30번까지 리스트 생성

for _ in range(28):  # 28명의 제출자 입력
    submit = int(input())  
    student.remove(submit)  # 제출한 학생을 리스트에서 제거

# 남아있는 두 학생(미제출자) 출력
for not_submitted in student:
    print(not_submitted)