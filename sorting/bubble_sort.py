
# Bubble Sort have 0(N^2) Time Complexity and 0(1) Space Complexity
def bubble_sort(arr):
    sort, end = True, len(arr) - 1
    while end > 0:
        for x in range(0, end):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
        end = end - 1
    return arr



if __name__ == '__main__':
    bubble_sort([5,2,8,5,6,3,9])
