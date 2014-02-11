import csv
import numpy as np

#csvfile = open('./sample_data/1-1.csv', 'r')
with open('./sample_data/1-1.csv', newline='') as f:
    sincyou = csv.reader(f, dialect='unix', delimiter=',')
    for row in sincyou:
        #print(','.join(row))
        print(row)


#    hist = {}
#    i = 0
#    for x in data:
#        i = i + 1
#        print(i)
#        print(x)
#        hist[x] = hist.get(x, 0) + 1
#print(hist)

data = np.loadtxt('./sample_data/1-1.csv', delimiter=',')
print(data)
hist, binedge = np.histogram(data)
print(hist, binedge)

#help(np.histogram)
