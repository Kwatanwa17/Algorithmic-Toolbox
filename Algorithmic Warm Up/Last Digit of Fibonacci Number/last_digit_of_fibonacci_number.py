# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    fib_list = []
    fib_list.append(0)

    if n > 0:
        fib_list.append(1)

    if n > 1:
        for i in range(2, n+1):
            fib_num = fib_list[i - 1] + fib_list[i - 2]
            fib_num = fib_num % 10
            fib_list.append(fib_num)

    return fib_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
