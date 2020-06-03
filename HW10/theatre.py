class Theatre:
        def __init__(self, file_name):
            self.filename = file_name
            self.matrix = list()
            with open(self.filename, 'r') as f:
                for line in f:
                    l = len(line) - 1
                    self.matrix.append(line[0: l].strip().split(sep=' '))

        def count_free(self):
            count = 0
            for arr in self.matrix:
                count += arr.count('0')
            return count

        def is_free_place(self, row, column):
            try:
                line = self.matrix[row - 1]
            except IndexError:
                raise ValueError(f'{row} row is incorrect')
            try:
                place = line[column - 1]
            except IndexError:
                raise ValueError(f'{column} column is incorrect')
            if place == '0':
                return True
            else:
                return False


if __name__ == '__main__':
    name = 'places.txt'
    theatre = Theatre(name)
    print(theatre.count_free())
    print(theatre.is_free_place(1, 3))
