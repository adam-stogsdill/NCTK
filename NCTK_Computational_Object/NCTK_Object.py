import numpy as np


class Filter():

    def __init__(self, filter_list):
        self.filter = np.asarray(filter_list)

    def __call__(self):
        return self.filter

    