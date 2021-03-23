class Solutions(object):
    def __init__(self, v):
        self.best_d = []
        self.v = [0] + v
        self.n = len(v)
        # a.1: best[i] denotes that the maximum number of coins when C_i is the last cup.
        self.best = [-1] * len(self.v)
        self.cups = [-1] * len(self.v)

    def part_a(self):
        # a.2
        self.best[0] = 0
        self.best[1] = 0
        self.best[2] = self.v[2]
        self.best[3] = self.v[2] + self.v[3]
        self.dp_a(self.n - 1)
        self.dp_a(self.n)

    def dp_a(self, idx):
        if self.best[idx] != -1:
            return self.best[idx]
        # a.3
        self.best[idx] = max(self.dp_a(idx - 3) + self.v[idx - 1] + self.v[idx],
                             self.dp_a(idx - 2) + self.v[idx])
        for i in range(4, self.n + 1):
            self.dp_a(i)

    def part_b(self):
        self.cups[0] = 0
        self.cups[1] = 0
        self.cups[2] = 1
        self.cups[3] = 1
        for i in range(4, self.n + 1):
            self.dp_b(i)

    def dp_b(self, idx):
        if self.cups[idx] != -1:
            return self.cups[idx]
        # case 1
        case_1 = self.best[idx - 2] + self.v[idx]
        # case 2
        case_2 = self.best[idx - 3] + self.v[idx - 1] + self.v[idx]
        # b.1
        if case_1 < case_2:
            self.cups[idx] = self.dp_b(idx - 3) + 1
        else:
            self.cups[idx] = self.dp_b(idx - 2) + 1
        return self.cups[idx]

    def print_solution(self):
        # b.2
        for i in range(self.n - 1, -1, -1):
            if (self.cups[i + 1] - self.cups[i]) == 1:
                print(i, end=' ')
        print()

    def part_c(self):
        self.best = [-1] * len(self.v)
        # c.2
        self.best[0] = 0
        self.best[1] = self.v[1]
        self.best[2] = self.v[1] + self.v[2]
        self.best[3] = self.v[2] + self.v[3]
        self.best[4] = max(self.v[1] + self.v[4], self.v[3] + self.v[4])
        for i in range(4, self.n + 1):
            # c.3
            self.best[i] = max(self.best[i - 4] + self.v[i - 1] + self.v[i],
                               self.best[i - 3] + self.v[i - 1] + self.v[i],
                               self.best[i - 3] + self.v[i],
                               self.best[i - 2] + self.v[i])

    def part_d(self):
        for i in range(self.n + 1):
            self.best_d.append([])
            for j in range(self.n + 1):
                self.best_d[i].append(-1)
        # d.2
        for i in range(self.n + 1):
            self.best_d[i][i] = self.v[i]
            if i + 1 <= self.n:
                self.best_d[i][i + 1] = max(self.v[i], self.v[i + 1])
        self.dp_d(1, self.n)

    def dp_d(self, i, j):
        if self.best_d[i][j] != -1:
            return self.best_d[i][j]
        # d.3
        self.best_d[i][j] = max(self.dp_d(i + 1, j - 1) + max(self.v[i], self.v[j]),
                                self.dp_d(i + 1, j) + self.v[i],
                                self.dp_d(i, j - 1) + self.v[j],
                                self.best_d[i][j])

        return self.best_d[i][j]


if __name__ == '__main__':
    v = [1, 3, 4, 1, 4, 5]
    n = len(v)
    solutions = Solutions(v)
    solutions.part_a()
    print(solutions.best)
    solutions.part_b()
    print(solutions.cups)
    solutions.print_solution()
    solutions.part_c()
    print(solutions.best)
    solutions.part_d()
    print(solutions.best_d[1][n])
