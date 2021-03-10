class Sorting:
    def bubble_sort(self, num_list):
        for i in range(len(num_list)):
            for j in range(i + 1, len(num_list)):
                if num_list[i] > num_list[j]:
                    num_list[i], num_list[j] = num_list[j], num_list[i]
        return num_list

    def bubble_sort_improvised(self, num_list):
        is_sorted = False
        for i in range(len(num_list)):
            for j in range(i + 1, len(num_list)):
                if num_list[i] > num_list[j]:
                    num_list[i], num_list[j] = num_list[j], num_list[i]
                    is_sorted = True
            if is_sorted:
                return num_list
        return num_list

if __name__ == "__main__":
    obj = Sorting()
    print(obj.bubble_sort([4, 3, 6, 1, 5, 2]))
