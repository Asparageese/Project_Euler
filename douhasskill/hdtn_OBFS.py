# Slightly Optimized HDTN divisor finder.
# Limits the amount of required checks, and mapped memory
# by working with the idea of bounds, and only preforming required
# checks to narrow bounds.

# This is done via a recursive method, if a HDTN is a common multiple of
# factors, then recurive division of that HDTN with respect to the factor
# should yield all divisors, as well as unique divisors, aka primes.
# keeping primes seperate should then be a method of finding primes from hdtns.

import numpy as np
import functools

samples = 10
domain = np.arange(1,samples)
domainC = [functools.reduce(lambda a,b:a+b,domain[:i+1]) for i in range(np.size(domain))]
domainC = np.array(domainC,dtype='object')[1:]
print(domainC)
