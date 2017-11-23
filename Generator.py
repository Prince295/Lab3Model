import numpy as np


class Generator():
    e = np.exp()
    z = 0
    zmax = e - 1

    def recursive_function(self):
        f1 = np.random.random()
        self.z = self.e ^ f1 - 1
        return self.z

    