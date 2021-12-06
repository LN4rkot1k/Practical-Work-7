def binom(M, N):
    if (M == 0) or (M == N):
        return 1
    else:
        return binom(M, N - 1) + binom(M - 1, N - 1)


n, m = map(int, input("Введите числа N и M: ").split())

if n >= m >= 0:
    print(binom(m, n))
else:
    print("Введены неправильные значения")
