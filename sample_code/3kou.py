import numpy as np
import math

data=np.array([6,4,6,6,6,3,7,2,2,8])
ave = np.average(data)
print("平均: ", ave)
devi = data - ave
print("偏差: ", devi)
devi_sq = pow(devi, 2)
print("偏差の２乗: ", devi_sq)
var = sum(devi_sq) / len(data)
print("偏差の２乗の平均=分散: ", var)
print("numpyだとこれ１個で分散: ", np.var(data))
sd = math.sqrt(var)
print("分散の平方根=標準偏差: ", sd)
print("numpyだとこれで標準偏差: ", np.std(data))

