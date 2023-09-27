def array_B(A):
    n = len(A)
    B = [1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                B[i] *= A[j]
    return B


A = list(map(int, input().split()))
B = array_B(A)
print(B)