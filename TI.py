import math
import sys
from math import log2, ceil


def encode_levenshtein(n: int) -> str:
    if n == 0:
        return "0"
    c, code = 1, ""
    while True:
        code = bin(n)[3:] + code
        n = ceil(log2(n + 1)) - 1
        if n == 0:
            break
        c += 1
    return "1" * c + "0" + code


def decode_levenshtein(code: str) -> int:
    ones = 0
    for c in code:
        if c == "0":
            break
        ones += 1
    if ones == 0:
        return 0
    n = 1
    offset = ones + 1
    for _ in range(ones - 1):
        new_n = int("1" + code[offset:offset + n], 2)
        offset += n
        n = new_n

    return n


def encode_elias(n: int) -> str:
    if n == 0:
        return "10"
    elif n == 1:
        return "11"
    else:
        part_1 = f'{n:b}'[1:]
        part_2 = f"{len(f'{n:b}'):b}"
        part_3 = '0' * (len(part_2) - 1)

        return part_3 + part_2 + part_1


def decode_elias(code: str) -> int:
    if code == '10':
        return 0
    elif code == '11':
        return 1
    else:
        zeros = 1
        for c in code:
            if c == '1':
                break
            zeros += 1
        code = code[zeros - 1:]
        orig_num_len = int(code[:zeros], 2)
        code = code[zeros:]

        return int('1' + code[:orig_num_len], 2)


line = sys.stdin.read().split()

if line[0] == 'cd':
    print(f'Введенное число: {line[0]}')

    if line[2] == 'lev':
        num = int(line[1])
        while num > 0:
            print(f'[log({num})] = {math.floor(math.log2(num))}')
            num = math.floor(math.log2(num))
        print(encode_levenshtein(int(line[1])))
    elif line[2] == 'el':
        print(encode_elias(int(line[1])))

elif line[0] == 'dc':
    print(f'Введенный код: {line[0]}')

    if line[2] == 'lev':
        print(decode_levenshtein(line[1]))
    elif line[2] == 'el':
        print(decode_elias(line[1]))
