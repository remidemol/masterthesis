#!/usr/bin/env python
# Author: Rémi DEMOL (github.com/remidemol)

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

dx = [0.05, 0.02, 0.01, 0.005]
erreurLinf = [0.000510934, 0.0000817468, 0.0000204343, 0.00000510661]

logdx = np.log10(dx)
logerr = np.log10(erreurLinf)

slope, intercept, r_value, p_value, std_err = stats.linregress(logdx,logerr)

plt.loglog(dx, erreurLinf, 'o')
plt.loglog(dx, 10**(slope*logdx+intercept), 'b-',label=r"$log(L\infty)$ = %.4f $log(\Delta x)$+ %0.4f ($R^2 = %0.3f)$" %(slope,intercept,r_value))

plt.ylabel('$log(L\infty)$')
plt.xlabel('$log(\Delta x)$')
plt.axis([0.001, 0.1, 0.000001, 0.001])
plt.grid(True,which="both",ls="-",color='grey')

plt.legend(loc=4)
plt.title("Evolution de la norme infinie")

plt.show()
