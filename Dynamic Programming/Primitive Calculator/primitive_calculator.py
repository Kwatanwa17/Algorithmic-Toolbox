# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6

    backtracks = [0] * (n + 1)
    # initial value
    backtracks[0] = 1

    for i in range(1, n):
        if i % 3 == 0:
            mult_3 = backtracks[int(i / 3)] + 1
        else:
            mult_3 = n

        if i % 2 == 0:
            mult_2 = backtracks[int(i / 2)] + 1
        else:
            mult_2 = n

        add_1 = backtracks[i - 1] + 1

        min_num = min(mult_3, mult_2, add_1)

        backtracks[i] = min_num

    return backtracks[1:]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
