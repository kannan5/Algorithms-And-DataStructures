def findTarget(arr, target):
    arr.sort()
    __findTarget(arr, target, [], 0)


def __findTarget(arr, target, pair, start):
    if target == 0:
        print(pair)
        return

    if start == len(arr):
        return

    for i in range(start, len(arr)):
        curr = arr[i]
        if curr > target:
            i = len(arr)
        if i > start and curr == arr[i - 1]:
            continue
        pair.append(curr)
        __findTarget(arr, target - curr, pair, i + 1)
        pair.pop()


if __name__ == '__main__':
    findTarget([1, 2, 3, 5, 2, 1, 5, 6, 7, 4], 5)
