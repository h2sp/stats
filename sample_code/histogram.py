import numpy as np
import pylab as pl

data = np.loadtxt('./sample_data/1-1.csv', delimiter=',')
hist, binedge = np.histogram(data, bins=[141,146,151,156,161,166,171])
print(hist)

# グラフ出すならこっち
pl.hist(data, bins=10, normed=True)
pl.show()

