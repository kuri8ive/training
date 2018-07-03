n = int(input())
*A, = input().split()
B = A[:]
for i in range(n):
    for j in range(n-1, i, -1):
        if A[j][1] < A[j-1][1]:
            A[j], A[j-1] = A[j-1], A[j]
print(*A)
print("Stable")
 
for i in range(n):
    minj = i
    for j in range(i, n):
        if B[j][1] < B[minj][1]:
            minj = j
    B[i], B[minj] = B[minj], B[i]
print(*B)
if A == B:
    print("Stable")
else:
    print("Not stable")
