import numpy as np
import matplotlib.pyplot as plt
#plt.plot() used for draw point in diagram

#plot with line
x_axis = np.array([0, 100])
y_axis = np.array([0, 200])

plt.plot(x_axis, y_axis)
plt.show()

#plot without line
plt.plot(x_axis, y_axis, 'o')
plt.show()