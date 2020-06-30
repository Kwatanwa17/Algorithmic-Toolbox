# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):

    nums = sorted(numbers, reverse = True)
    iter = 1

    if len(nums) > 1:
        while iter == 1:
            iter = 0
            for i in range(0, len(nums)-1):
                a, b = str(nums[i]), str(nums[i + 1])
                ab, ba = a + b, b + a
                if ab == ba or ab > ba:
                    # Do not change the order
                   continue
                else:
                    # Change the order
                    nums[i] = b
                    nums[i + 1] = a
                    iter = 1

    return int(''.join(str(e) for e in nums))



if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
