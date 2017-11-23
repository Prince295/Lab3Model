import numpy as np


class Generator():
    e = np.exp()
    z = 0
    zmax = e - 1

    def recursive_function(self):
        f1 = np.random.random()
        self.z = self.e ^ f1 - 1
        return self.z
    def array_of_func(self,n):
        for i in range(n):
            self.array.append(self.recursive_function(self))
        self.array.sort()
        return self.array
