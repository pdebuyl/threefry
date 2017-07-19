"""
================================
Showing the uniform distribution
================================

Example of drawing random uniform number with threefry.
"""

import threefry
import matplotlib.pyplot as plt

r = threefry.rng(673144720833845866)

data = [r.random_uniform() for i in range(5000)]

plt.hist(data, bins=32, normed=True)
plt.xlabel(r'$x$')
plt.ylabel(r'$P(x)$')
plt.show()
