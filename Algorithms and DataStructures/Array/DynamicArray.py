import ctypes


class DynamicArray:

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.capacity

    def __getitem__(self, elem):
        if not (0 <= elem < self.n):
            return IndexError("Enter the Valid Index")
        return self.A[elem]

    def append(self, elem):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = elem
        self.n += 1

    def make_array(self, new_size):
        return (new_size * ctypes.py_object)()

    def _resize(self, new_size):
        new_array = self.make_array(new_size)
        # B = self.A

        for z in range(self.n):
            new_array[z] = self.A[z]
        self.A = new_array
        self.capacity = new_size


if __name__ == "__main__":
    arr = DynamicArray()





