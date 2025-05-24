import matplotlib.pyplot as plt
import numpy as np

# print(plt.__version__) # check version matplotlib library

x_axis = np.array([0, 100])
y_axis = np.array([0, 250])

plt.plot(x_axis, y_axis)
plt.show()