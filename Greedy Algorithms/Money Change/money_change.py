# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    count = 0
    for coin in [10, 5, 1]:
        while True:
            if money < coin:
                break
            money = money - coin
            count += 1

    return count


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
