L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

국어 = (A+C - 1) // C
수학 = (B+D - 1) // D

숙제 = max(국어, 수학)
print(L - 숙제)