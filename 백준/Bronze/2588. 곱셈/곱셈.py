a = int(input())
b = int(input())

k = str(b)
Q = int(int((k[2])) * a)
W = int(int((k[1])) * a)
E = int(int((k[0])) * a)
R = int(int(Q)+int(str(W)+"0")+int(str(E)+"00"))

print(Q)
print(W)
print(E)
print(R)