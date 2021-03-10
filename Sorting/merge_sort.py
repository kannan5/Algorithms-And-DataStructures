class Sorting:

    def merge_sort(self, arr):

        if len(arr) > 1:  # we need min 2 element to compare and sort
            mid = len(arr) // 2

            # Split array into 2 Sub Array
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr


if __name__ == "__main__":
    obj = Sorting()
    print(obj.merge_sort([3, 2, 6, 4, 1]))
