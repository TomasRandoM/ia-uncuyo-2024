import random

class Environment:
    def __init__(self, n):
        self.n = n
        self.env = [0 for _ in range(n)]
        self.cost = self.h(self.env)
        for i in range(0, n):
            self.env[i] = random.randint(0, n - 1)

    def h(self, env):
        attacks = 0
        m = len(env)
        for i in range(0, m):
            for j in range(i + 1, m):
                if env[i] == env[j] or abs(env[j] - env[i]) == abs(j - i):
                    attacks += 1
        return attacks