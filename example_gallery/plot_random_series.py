"""
======================
Drawing random numbers
======================

Example of drawing random uniform number with threefry.
"""

import threefry
import matplotlib.pyplot as plt

r = threefry.rng(8760396957664838051)

data = [r.random_uniform() for i in range(10)]

plt.plot(data)

plt.show()
