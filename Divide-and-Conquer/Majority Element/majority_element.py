# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2  # Finding the mid of the array
            L = arr[:mid]  # Dividing the array elements
            R = arr[mid:]  # into 2 halves

            merge_sort(L)  # Sorting the first half
            merge_sort(R)  # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    merge_sort(elements)

    m = int(len(elements)/2)

    center = elements[m]

    left_half= elements[:m]
    right_half = elements[m+1:]

    left_count = 0
    right_count = 0

    for i in left_half:
        if center == i:
            left_count += 1

    for i in right_half:
        if center == i:
            right_count += 1

    if (left_count + right_count + 1) > m:
        return 1
    else:
        return 0





if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
