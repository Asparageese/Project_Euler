import numpy as np

samples = 5000
domain = np.arange(1,samples)
yList = []
for i in range(np.size(domain)):
    yList.append(np.sum(domain[:i+1]))
yList = np.array(yList)[2:]
dCache = []
for x in yList:
    acache = []
    if x % 2 == 0:
        a = 2
        b = x / a
    else:
        a = 3
        b = x / a
    dSet = np.arange(a,b)
    for d in dSet:
        if x % d == 0:
            acache.append(d)
    dCache.append(np.size(acache))
print(np.max(dCache))

