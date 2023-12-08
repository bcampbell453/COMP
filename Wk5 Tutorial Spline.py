# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:10:26 2023

@author: blath
"""

# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math
import random

x = np.array([0.  , 0.06666667, 0.13333333, 0.2 ,  0.26666667, 0.33333333,
     0.4 , 0.46666667, 0.53333333, 0.6 ,  0.66666667, 0.73333333,
     0.8 , 0.86666667, 0.93333333, 1.  , ])

y = np.array([ 0.00000000e+00,  7.78309056e-01,  1.24040577e+00,  1.24494914e+00,
      8.90566050e-01,  4.33012702e-01,  1.12256994e-01,  4.54336928e-03,
     -4.54336928e-03, -1.12256994e-01, -4.33012702e-01, -8.90566050e-01,
     -1.24494914e+00, -1.24040577e+00, -7.78309056e-01, -4.89858720e-16])

#Plotting data
plt.title('Experimental data')
plt.scatter(x,y)
plt.show()

# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate

# array containing the points where we want to evaluate the 
# intepolation
x_int = np.linspace(0,1,num=64)

# generate linear interpolant 
f_lin = interpolate.interp1d(x, y, kind='linear')
# evaluate linear interpolan at the desiderd points
y_int_lin = f_lin(x_int)

# generate spline interpolant 
f_spline  = interpolate.splrep(x, y, s=0)
#s controls the smoothness of the spline, higher s is smoother
#Lower s means it fits more closely to provided data
# evaluate spline interpolan at the desiderd points
y_int_spline = interpolate.splev(x_int, f_spline, der=0)

# plot results
plt.figure()
plt.title('Results')
plt.plot(x,y,'gh',ms=10)
plt.plot(x_int,y_int_lin,'r.',x_int,y_int_spline,'b.')
plt.xlabel('x')
plt.ylabel('y')

# plot a zoom
plt.figure()
plt.title('zoomed section of results')
plt.plot(x,y,'gh',ms=10)
plt.plot(x_int,y_int_lin,'r.',x_int,y_int_spline,'b.')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0.05,0.3)
plt.ylim(0.5,1.5)

plt.show()