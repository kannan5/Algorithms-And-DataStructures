class Sorting:
    def swap(self, arr, pos1, pos2):
        arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
        return

    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_ind = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_ind]:
                    min_ind = j
            if arr[i] != arr[min_ind]:
                arr[i], arr[min_ind] = arr[min_ind], arr[i]
        return arr


if __name__ == "__main__":
    obj = Sorting()
    print(obj.selection_sort([2, 7, 5, 4, 3]))
