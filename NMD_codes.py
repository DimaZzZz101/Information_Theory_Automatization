import sys
import math


def C(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0


# Существование.
def Hamming(N, M, D):
    print('IN HAMMING')
    ans = False
    t = math.ceil((D - 1) / 2)
    print(f't = {t}')
    summ = 0
    for i in range(t + 1):
        summ += C(N, i)
    print(f'A(n, 2t+1) <= {2 ** N / summ} <= {math.floor(2 ** N / summ)}\n')
    if M <= math.floor(2 ** N / summ):
        ans = True

    return ans


# Существование.
def Djoshi(N, M, D):
    print('IN DJOSHI')
    ans = False
    print(f'A(n, d) <= {2 ** (N - D - 1)} <= {math.floor(2 ** (N - D - 1))}\n')
    if M <= math.floor(2 ** (N - D - 1)):
        ans = True
    return ans


# Оптимальность.
def Varsh_Gilb(N, M, D):
    print('IN VARSHAMOV_GILBERT')
    ans = False
    t = math.ceil((D - 1) / 2)
    print(f't = {t}')
    summ = 0
    for i in range(2 * t + 1):
        summ += C(N, i)

    print(f'A(n, 2t+1) <= {2 ** N / summ} <= {math.ceil(2 ** N / summ)}\n')
    if M >= math.ceil(2 ** N / summ):
        ans = True
    return ans


# Существование.
def Plotkin(N, M, D):
    print('IN PLOTKIN')
    ans = False
    dumb = False
    if 2 * D < N:
        dumb = True
        print('Проверку 2d > n - не успешно.')
        return ans, dumb
    print('Проверка 2d > n - успешно.')
    print(f'A(n, d) <= {2 * D / (2 * D - N)} <= {math.floor(2 * D / (2 * D - N))}\n')
    if M <= math.floor(2 * D / (2 * D - N)):
        ans = True
    return ans, dumb


def get_answers(hamming, djoshi, varsh_gilb, plotkin, N, M, D):
    if hamming:
        print(f'FOR N = {N}, M = {M}, D = {D} => HAMMING -> OK')
    else:
        print(f'FOR N = {N}, M = {M}, D = {D} => HAMMING -> NO')

    if djoshi:
        print(f'FOR N = {N}, M = {M}, D = {D} => DJOSHI -> OK')
    else:
        print(f'FOR N = {N}, M = {M}, D = {D} => DJOSHI -> NO')

    if varsh_gilb:
        print(f'FOR N = {N}, M = {M}, D = {D} => VARSH_GILB -> OK')
    else:
        print(f'FOR N = {N}, M = {M}, D = {D} => VARSH_GILB -> NO')

    if plotkin[0]:
        print(f'FOR N = {N}, M = {M}, D = {D} => PLOTKIN -> OK')
    elif plotkin[1]:
        print(f'FOR N = {N}, M = {M}, D = {D} => PLOTKIN -> NO, так как 2 * D < N')
    else:
        print(f'FOR N = {N}, M = {M}, D = {D} => PLOTKIN -> NO')


def get_verdict(hamming, djoshi, varsh_gilb, plotkin):
    if hamming and djoshi and plotkin[0]:
        if varsh_gilb:
            print('Код может существовать и он может быть оптимальным.')
        else:
            print('Код может существовать, но он не оптимальный.')
    else:
        print('Код не существует.')


if __name__ == '__main__':
    line = sys.stdin.read().split()

    N = int(line[0])
    M = int(line[1])
    D = int(line[2])

    hamming = Hamming(N, M, D)
    djoshi = Djoshi(N, M, D)
    varsh_gilb = Varsh_Gilb(N, M, D)
    plotkin = Plotkin(N, M, D)

    print('Результаты:')
    get_answers(hamming, djoshi, varsh_gilb, plotkin, N, M, D)

    print('\nВердикт:')
    get_verdict(hamming, djoshi, varsh_gilb, plotkin)
