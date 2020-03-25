import heapq


class MedianFinder:

    def __init__(self):
        self.nums = []

    def add_num(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def find_median(self) -> float:
        l = len(self.nums)
        if l > 0:
            med1 = int((l - 1) / 2)
            if l % 2 == 0:
                med2 = int(med1 + 1)
                return round((self.nums[med1] + self.nums[med2])/2, 1)
            else:
                return self.nums[med1]
        else:
            return round(self.nums[0], 1)
