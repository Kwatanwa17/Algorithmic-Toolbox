# python3

from itertools import product
from sys import stdin


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    # if len(values) < 3 or sum(values) % 3 != 0
    if len(values) < 3 or sum(values) % 3 != 0:
        return 0
    else:
        subset = int(sum(values)/3)

        # Knapsack problem with no repetitions
        souvenirs = sorted(list(values))[::-1]
        log = [0] * 3
        base = int(sum(values)/3)

        for idx, capacity in enumerate([base, base*2, base*3]):

            # initialization
            value = []
            for _ in range(len(souvenirs) + 1):
                value.append([0] * (capacity + 1))

            # fill in the matrix
            for i in range(1, len(souvenirs) + 1):
                for w in range(1, capacity + 1):
                    value[i][w] = value[i - 1][w]
                    if souvenirs[i - 1] <= w:
                        val = value[i - 1][w - souvenirs[i - 1]] + souvenirs[i - 1]
                        if value[i][w] < val:
                            value[i][w] = val

            # break if the optimal value is not the capacity
            if value[-1][-1] != capacity:
                break
            else:
                log[idx] = 1

            # # backtrace
            # optimal_val = value[-1][-1]
            # col = capacity
            # for row in range(len(souvenirs) - 1, -1, -1):
            #     excluded_s = souvenirs[row]
            #     if value[row][col] != optimal_val:
            #         # excluded_s is used
            #         # discount the excluded souvenir
            #         col = col - excluded_s
            #         # change the optimal val
            #         optimal_val = value[row][col]
            #         # set 1 to the used array
            #         used[row] = 1

            # # break if the total souvenir iks inferior to the capacity
            # if sum(souvenirs) < capacity:
            #     break

            # # delete used souvenirs\
            # new_souvenirs = []
            # for idx, is_used in enumerate(used):
            #     if is_used == 0:
            #         new_souvenirs.append(souvenirs[idx])
            #
            # # update the souvenirs and the used array
            # souvenirs = new_souvenirs
            # used = [0] * len(souvenirs)

        # check if all items are used
        if sum(log) == 3:
            return 1
        else:
            return 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
