import matplotlib.pyplot as plt
import numpy as np

# statistical constants for XMR charts
d2 = 1.128
D3 = 0
D4 = 3.267

class XMR:
    """ class to create a simple XMR control chart from an array of data """
    def __init__(self, data, index=None):

        self.data = data
        if index is None:
            index = list(range(len(self.data)))
        self.index = index
        self.data_mr = self.moving_range(data)
    
    @staticmethod
    def moving_range(data):
        return abs(data[1:] - data[:-1])

    @staticmethod
    def plot_chart(data, index, center, ucl, lcl, axes=None, **kwargs):
        if axes is None:
            fig,axes = plt.subplots(1,1)

        axes.plot(index, data, marker='o', **kwargs)
        axes.axhline(center, **kwargs)
        axes.axhline(ucl, **kwargs)
        axes.axhline(lcl, **kwargs)
        return axes

    def xchart(self, axes=None, **kwargs):
        xbar = np.mean(self.data)
        mrbar = np.mean(self.data_mr)
        ucl = xbar + 3*mrbar/d2 
        lcl = xbar - 3*mrbar/d2

        axes = self.plot_chart(self.data, self.index, xbar, ucl, lcl, axes, **kwargs)  
        return axes

    def mrchart(self, axes=None, **kwargs):
        mrbar = np.mean(self.data_mr)
        ucl = D4*mrbar
        lcl = D3*mrbar

        axes = self.plot_chart(self.data_mr, self.index[1:], mrbar, ucl, lcl, axes, **kwargs)
        return axes
