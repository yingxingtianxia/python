#!/usr/bin/env python
#--coding: utf8--
import numpy as np
import matplotlib.pyplot as plt
x = y =np.arange(-11, 11, 0.1)
x, y = np.meshgrid(x, y)
for i in range(1, 11):
    plt.contour(x, y, x**2+y**2, [i**2])
    plt.axis('scaled')

plt.show()