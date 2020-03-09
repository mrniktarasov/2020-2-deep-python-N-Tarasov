from itertools import zip_longest


class ArrAddSub(list):
    def __init__(self, *nums):
        self.inList = list(nums)[:]
        self.sum = sum(self.inList)

    def __add__(self, other):
        ret_list = []
        for i1, i2 in zip_longest(self.inList, other.inList):
            if i1 is None:
                i1 = 0
            if i2 is None:
                i2 = 0
            ret_list.append(i1 + i2)
        return ret_list

    def __sub__(self, other):
        ret_list = []
        for i1, i2 in zip_longest(self.inList, other.inList):
            if i1 is None:
                i1 = 0
            if i2 is None:
                i2 = 0
            ret_list.append(i1 - i2)
        return ret_list

    def __eq__(self, other):
        if self.sum == other.sum:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.sum == other.sum:
            return False
        else:
            return True

    def __lt__(self, other):
        if self.sum < other.sum:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.sum > other.sum:
            return True
        else:
            return False

    def __le__(self, other):
        if self.sum <= other.sum:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.sum >= other.sum:
            return True
        else:
            return False
