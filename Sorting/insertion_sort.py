class Sorting:
    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            curr = arr[i]
            j = i - 1
            while j >= 0 and curr < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = curr
        return arr


if __name__ == "__main__":
    obj = Sorting()
    print(obj.insertion_sort([3, 2, 5, 7, 6]))
