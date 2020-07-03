# python3

from random import randint


def partition3(array, left, right):
    # print(array, left, right)
    x = array[left]
    # m1 is the last position where x < array[j]
    m1 = left
    m2 = left

    for i in range(left + 1, right + 1):

        if array[i] < x:
            if i == m2:
                m1 += 1
                m2 += 1
                array[m1], array[m2] = array[m2], array[m1]
                array[i], array[m1] = array[m1], array[i]

            else:
                # add 1 to j so that j becomes the next position to the current j
                m1 += 1
                m2 += 1
                # swap i and j
                array[i], array[m1] = array[m1], array[i]

        elif array[i] == x:
            # add 1 to j so that j becomes the next position to the current j
            m2 += 1
            # swap i and j
            array[i], array[m2] = array[m2], array[i]

    # swap left and m1
    array[left], array[m1] = array[m1], array[left]

    # print(m1, m2)
    return m1, m2


def dijkstra_partition3(array, left, right):
    """
    3-way partition from https://www.cs.princeton.edu/courses/archive/fall12/cos226/demo/23DemoPartitioningDijkstra.pdf
    """
    # partitioning item (pivot)
    v = array[left]
    # left most and right most items
    lt = left
    gt = right
    # start position
    i = left

    while True:
        if gt < i:
            break

        if array[i] < v:
            # swap lt and i
            array[lt], array[i] = array[i], array[lt]
            lt += 1
            i += 1
        elif array[i] > v:
            # swap gt and i
            array[gt], array[i] = array[i], array[gt]
            gt -= 1
        else:
            i += 1

    return lt, gt


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    # print('k:', k)
    # push array[k] to the first position (pivot)
    array[left], array[k] = array[k], array[left]
    m1, m2 = dijkstra_partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
