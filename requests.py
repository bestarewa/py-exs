#/usr/bin/env python
"""
__author__ = 'Abba y Abddullahi , abbayabdullahi68@gmail.com'
__copyright__ = 'copygright,  (c) ay abdullahi'
__version__ = 'o.2t'
"""
import numpy as np
import matplotlib.pyplot as plt
a = np.arange(0., 10., 0.4)
plt.plot(a,a, 'r--',a, a**4, 'bs',a, a**6, 'g^')
plt.title('good result')
plt.show()

