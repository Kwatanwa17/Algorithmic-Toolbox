# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6

    backtracks = [0] * n

    for i in range(1, n):
        if (i + 1) % 3 == 0:
            mult_3 = backtracks[int((i + 1) / 3) - 1] + 1
        else:
            mult_3 = n

        if (i + 1) % 2 == 0:
            mult_2 = backtracks[int((i + 1) / 2) - 1] + 1
        else:
            mult_2 = n

        add_1 = backtracks[i - 1] + 1

        min_num = min(mult_3, mult_2, add_1)

        backtracks[i] = min_num

    result = [n]

    for num in list(range(backtracks[-1]))[::-1]:
        if num == 0:
            if 1 not in result:
                result.append(1)
            break

        for idx, i in enumerate(backtracks):
            if i == num:
                result.append(idx + 1)
                break

    return result[::-1]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
