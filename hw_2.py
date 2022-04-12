from collections.abc import Iterable


def flat_generator(items, ignore_types=(str, bytes)):
    """
      str, bytes - являются итерируемыми объектами,
       но их хотим возвращать целыми
    """
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flat_generator(x)
        else:
            yield x


nested_list = [['a', 'b', 'c'], ['d', [1, 101, 222], 'e', 'f'], [1, 2, None]]

if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
