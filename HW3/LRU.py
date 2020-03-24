from collections import OrderedDict


class ICache:
    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> str:
        try:
            return self.cache[key]
        except KeyError:
            raise ValueError('Wrong key {}'.fromat(key))

    def set(self, key: str, value: str) -> None:
        if self.capacity > 0:
            self.cache[key] = value
            self.capacity -= 1
        else:
            self.cache.popitem()
            self.cache[key] = value

    def delete(self, key: str) -> None:
        if self.capacity > 0:
            try:
                self.cache.move_to_end(key)
                self.cache.popitem()
            except KeyError:
                raise ValueError('Wrong key {}'.fromat(key))
            self.capacity += 1
        else:
            return ''
