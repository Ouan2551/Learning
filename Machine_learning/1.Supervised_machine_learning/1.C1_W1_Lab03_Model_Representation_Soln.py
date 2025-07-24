import numpy as np
import matplotlib.pyplot as plt
plt.style.use(r'D:\Important files Nannaphat\coding\Learning\Machine_learning\1.Supervised_machine_learning\1.deeplearning.mplstyle')

# example this is house prize / area
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print("x_train : ", x_train)
print("y_train : ", y_train)

# m is the number of training examples
print(f"x_train.shape: {x_train.shape}")
m = x_train.shape[0]
# or using like this m = len(x_train)
print(f"Number of training examples is: {m}")

# training example x_i, y_i
i = 0 # Change this to 1 to see (x^1, y^1)
x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

# plotting the data
plt.scatter(x=x_train, y=y_train, marker='x', c='r')
plt.title("Housing Prices")
plt.ylabel("Price")
plt.xlabel("Area")
plt.show()

# Model function (linear regression)
# f(w,b)(x^i) = w*(x^i) + b
w = 100 # slope
b = 100
# different value w and b give you different straight line
# change w and b to find line that fit with data
print(f"w: {w}")
print(f"b: {b}")

def compute_model_output(x, w, b): # output linear model
    """
    Computes the prediction of a linear model
    Args:
        x (ndarray (m,)): Data, m examples 
        w,b (scalar)    : model parameters  
    Returns
        y (ndarray (m,)): target values
    """
    # just high school want to draw graph
    m = x.shape[0]
    f_wb = np.zeros(m) # will return a one-dimensional numpy array with entries
    for i in range(m):
        f_wb[i] = w * x[i] + b # imagine y = mx + c
        
    return f_wb

tmp_f_wb = compute_model_output(x_train, w, b,)

# Plot our model prediction
plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction')

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')

# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price')
# Set the x-axis label
plt.xlabel('Size')
plt.legend()
plt.show()

# Prediction
# w and b get from train (find best value)
# then put value w and b into code for prediction (simple code)
w = 100
b = 100
x_i = 5.0
cost_1200_sqft = w * x_i + b
print(f"${cost_1200_sqft:.0f} thousand dollars")