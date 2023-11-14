import math, sys
sys.setrecursionlimit(200000)

def divide_to_rc(n):
    row = int(math.sqrt(n))

    while (n % row) != 0:
        row -= 1
    col = int(n / row)
    
    return row, col

# Young table with row major array
class row_pic():
    def __init__(self, init_array, row, column):
        self.array = init_array
        self.row = row
        self.column = column
        self.visited = []

    def idx2rc(self, k):
        i = k // self.column
        j = k % self.column
        return (i, j)

    def rc2idx(self, i, j):
        return i * self.column + j

    def get_at(self, i, j):
        if (i >= self.row) or (j >= self.column):
            return -1
        return self.array[self.rc2idx(i, j)]

    def set_at(self, i, j, k):
        self.array[self.rc2idx(i, j)] = k

    def __str__(self):
        result = ""
        for i in range(self.row):
            for j in range(self.column):
                result += str(self.get_at(i, j)) + ","
            result += "\n"
        return result

    def sift_down(self, i, j):
        next_col = self.get_at(i, j + 1)
        next_row = self.get_at(i + 1, j)

        max_neighbor = (0, 0)
        if next_col > next_row:
            max_neighbor = (i, j + 1)
        else:
            max_neighbor = (i + 1, j)

        if self.get_at(i, j) < self.get_at(max_neighbor[0], max_neighbor[1]):
            (self.array[self.rc2idx(i, j)], self.array[self.rc2idx(max_neighbor[0], max_neighbor[1])]) = (
            self.array[self.rc2idx(max_neighbor[0], max_neighbor[1])], self.array[self.rc2idx(i, j)])

            self.sift_down(max_neighbor[0], max_neighbor[1])
            
    def sort_sift_down(self, i, j):
        next_col = self.get_at(i, j + 1)
        next_row = self.get_at(i + 1, j)

        max_neighbor = (0, 0)
        if next_row > next_col and (i+1,j) not in self.visited:
            max_neighbor = (i+1, j)
        elif (i,j+1) not in self.visited:
            max_neighbor = (i, j+1)
        else:
            return

        if self.get_at(i, j) < self.get_at(max_neighbor[0], max_neighbor[1])    :
            (self.array[self.rc2idx(i, j)], self.array[self.rc2idx(max_neighbor[0], max_neighbor[1])]) = (
            self.array[self.rc2idx(max_neighbor[0], max_neighbor[1])], self.array[self.rc2idx(i, j)])

            self.sort_sift_down(max_neighbor[0], max_neighbor[1])

    def BuildYoungTable(self):
        for i in range(self.row - 1, -1, -1):
            for j in range(self.column - 1, -1, -1):
                self.sift_down(i, j)
                
    def young_sort(self):
        self.BuildYoungTable()
        
        for i in range(self.row-1, -1, -1):
            for j in range(self.column-1, -1,-1):
                # swap
                (self.array[self.rc2idx(i,j)], self.array[0]) = (self.array[0], self.array[self.rc2idx(i,j)])
                
                # adding i,j to visited
                self.visited.append((i,j))
            
                # sift down 0,0
                self.sort_sift_down(0,0)