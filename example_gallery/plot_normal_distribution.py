"""
===============================
Showing the normal distribution
===============================

Example of drawing normally distributed random number with threefry.
"""

import threefry
import matplotlib.pyplot as plt

r = threefry.rng(8255078853756962490)

data = [r.random_normal() for i in range(5000)]

plt.hist(data, bins=32, normed=True)
plt.xlabel(r'$x$')
plt.ylabel(r'$P(x)$')
plt.show()
