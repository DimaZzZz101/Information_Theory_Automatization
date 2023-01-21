import sys


def restore_symbol(code):
    answer = list(code)

    n = len(code) + 1
    k = n + 1

    print(f'n = {n}', f'k = {k}', sep='\n')

    ones_count = 0
    pos = 1
    pos_sum = 0

    for symbol in code:
        if symbol == '1':
            ones_count += 1
            pos_sum += pos
        pos += 1

    delta_b = (0 - pos_sum % k) % k

    print(f'||b|| = {ones_count}',
          f'w_b = {pos_sum}',
          f'(w_b)mod{k} = {pos_sum % k}',
          f'Δ_b = (w_a - w_b)mod{k} = (0 - {pos_sum % k})mod{k} = {delta_b}', sep='\n')

    if delta_b <= ones_count:
        print(f'Δb <= ||b||, значит выпал "0", а справа от него Δb = {delta_b} единиц:')
        i = len(answer) - 1
        while delta_b > 0:
            if answer[i] == '1':
                delta_b -= 1
            i -= 1
        answer.insert(i + 1, '[0]')
    else:
        print(f'Δb > ||b||, значит выпала "1", а справа от нее n - Δb = {n - delta_b} нулей:')
        i = len(answer) - 1
        count = n - delta_b
        while count > 0:
            if answer[i] == '0':
                count -= 1
            i -= 1
        answer.insert(i + 1, '[1]')

    print(''.join(answer))


def remove_symbol(code):
    k = len(code)
    n = k - 1

    print(f'n = {n}', f'k = {k}', sep='\n')

    ones_count = 0
    pos = 1
    pos_sum = 0

    for symbol in code:
        if symbol == '1':
            ones_count += 1
            pos_sum += pos
        pos += 1

    delta_b = pos_sum % k

    print(f'||b|| = {ones_count}',
          f'w_b = {pos_sum}',
          f'Δb = (w_b)mod{k} = {delta_b}', sep='\n')

    if delta_b == ones_count:
        print(f'Δb = ||b||, => лишний первый:')
        code = '_' + code[1:]

    elif delta_b == 0:
        print(f'Δb = 0, => лишний последний:')
        code = code[:1] + '_'

    elif delta_b < ones_count:
        print(f'Δb < ||b||, значит добавлен "0", а после него Δb = {delta_b} единиц:')
        i = len(code) - 1
        while delta_b > 0:
            if code[i] == '1':
                delta_b -= 1
            i -= 1
        code = code[:i] + '_' + code[i + 1:]
        # code = code.replace(code[i], '_', 1)

    elif delta_b > ones_count:
        print(f'Δb > ||b||, значит добавлена "1", а после нее n + 1 - Δb = {n + 1 - delta_b} нулей:')
        i = len(code) - 1
        count = n + 1 - delta_b
        while count > 0:
            if code[i] == '0':
                count -= 1
            i -= 1
        # code = code.replace(code[i], '_', 1)
        code = code[:i] + '_' + code[i + 1:]

    print(code)


if __name__ == '__main__':
    line = sys.stdin.read().split()

    mode = line[0]
    code = line[1]

    if mode == 'restore':
        restore_symbol(code)

    elif mode == 'remove':
        remove_symbol(code)
