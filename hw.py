nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None],]


class FlatIterator:
    def __init__(self, initial_list):
        self.isStopped = False
        self._list = initial_list
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.isStopped:
            while self.i < len(self._list):
                if self.j >= len(self._list[self.i]):
                    self.i += 1
                    self.j = 0
                    continue

                x = self._list[self.i][self.j]
                self.j += 1
                return x
            self.isStopped = True
        raise StopIteration


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

