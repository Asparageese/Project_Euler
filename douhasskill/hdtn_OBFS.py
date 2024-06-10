# Slightly Optimized HDTN divisor finder
# I will be attempting to use primes number to reduce the amount of computations.
# By computing the amount of primes present within half of the range,
# All possible unique factors of the range should be implied to exist
# within that point.
# A latex document as been written.
# The following is python prototype code.
import numpy as np
import functools

samples = 10
domain = np.arange(2,samples)
ydomain = [functools.reduce(lambda a,b: a+b, domain[:i+1]) for i in range(np.size(domain))]


