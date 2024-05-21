import numpy as np

samples = 10
domain = np.arange(1,samples)
yList = []
for i in range(np.size(domain)):
    yList.append(np.sum(domain[:i+1]))
yList = np.array(yList)[2:]

def yieldDivisors(hdtnSet):
    hitFn = lambda mul,x,hdtn: 1 if (hdtn == x*mul) else 0
    cache = []
    for hdtnNum in hdtnSet:
        if hdtnNum%2 == 0:
            mulSet = np.arange(2,(hdtnNum/2)+1)
        else:
            mulSet = np.arange(3,(hdtnNum/3)+1)
        pairing = list(zip(mulSet,reversed(mulSet)))
        cacheA = []  
        for p in pairing:
            if hitFn(p[0],p[1],hdtnNum) == 1:
                cacheA.append([p[0],hdtnNum])
        cache.append(cacheA)
    return cache

test = yieldDivisors(yList)

# This list can be treated as a linked mapping of the divisors, hence taking the last hdtn to produce a hit
# and simple running backwards through the mapping yields a path, where the number of steps taken is equal
# to the number of divisors.

def dPWalk(dset):
    dset = np.array(dset)
    lastHit = dset[-1][1][1]
    mPrimes = np.where(lastHit == dset)
    for x in mPrimes:
        print(dset[x])

dPWalk(test)

