from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __next__(self):
        try:
            response = self._data[self._index]
            self._index += 1
            return response
        except IndexError:
            raise StopIteration()
