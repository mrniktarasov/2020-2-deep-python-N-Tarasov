class ArrAddSub(list):
    def __init__(self, *args):
        self.inList = *args[::]

    def __add__(self, other):
        retls = []
        for i1, i2 in self.inList, other:
            retls.append(i1 - i2)
        return retls
