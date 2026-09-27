"""เเปลงดอกไม้"""
L, N = map(int, input().split())

k = 1

while True:
    cells = (L * (L + 1) // 2) + (k - 1) * (L * L)

    if N <= cells:
        print(k)
        break

    N = N - cells
    k = k + 1
