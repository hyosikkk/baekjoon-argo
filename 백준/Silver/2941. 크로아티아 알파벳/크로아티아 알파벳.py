arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for e in arr:
    a = a.replace(e, '*')  # 하나의 문자로 대체

print(len(a))