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

    def xlimits(self):
        mrbar = np.mean(self.data_mr)
        xbar = np.mean(self.data)
        ucl = xbar + 3*mrbar/d2
        lcl = xbar - 3*mrbar/d2
        return xbar, ucl, lcl

    def xchart(self, axes=None, **kwargs):
        xbar, ucl, lcl = self.xlimits()

        axes = self.plot_chart(self.data, self.index, xbar, ucl, lcl, axes, **kwargs)  
        return axes

    @staticmethod
    def out_of_control_limits(data, index, ucl, lcl):

        if not isinstance(data, list):
            data = list(data)
        if not isinstance(index, list):
            index = list(index)
        
        ooc_points = []
        ooc_index = []
        for i,point in enumerate(data):
            if point < lcl or point > ucl:
                ooc_points.append(data.pop(i))
                ooc_index.append(index.pop(i))
        return ooc_points, ooc_index, data, index

    def mrlimits(self):
        mrbar = np.mean(self.data_mr)
        ucl = D4*mrbar
        lcl = D3*mrbar
        return mrbar, ucl, lcl

    def mrchart(self, axes=None, **kwargs):
        mrbar, ucl, lcl = self.mrlimits()
        data = self.data_mr
        index = self.index[1:]
        ooc = (data<lcl) | (data>ucl)
        ooc_points = data[ooc]
        ooc_index = index[ooc]

        while any(ooc):
            data = data[~ooc]
            index = index[~ooc]
            mrbar = np.mean(data)
            ucl = D4*mrbar
            lcl = D3*mrbar
            ooc = (data<lcl) | (data>ucl)
            ooc_points = np.append(ooc_points, data[ooc])
            ooc_index = np.append(ooc_index, index[ooc])

        axes = self.plot_chart(self.data_mr, self.index[1:], mrbar, ucl, lcl, axes, **kwargs)
        axes.scatter(x=ooc_index, y=ooc_points, zorder=10, marker='X', color='red')
        print(ooc_points)
        print(ooc_index)
        return axes
