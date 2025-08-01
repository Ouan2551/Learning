# import library
import numpy as np
import matplotlib.pyplot as plt

# generate some simple data
x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([300.0, 500.0, 700.0, 900.0])

# cost function (measure square error)
def compute_cost(x, y, w, b):
    m = len(x)
    cost = 0.0
    for i in range(m):
        f_wb = w * x[i] + b
        cost += (f_wb - y[i])**2
    return cost / (2*m)

# gradients
def compute_gradients(x, y, w, b):
    m = len(x)
    dj_dw = 0.0
    dj_db = 0.0
    
    for i in range(m):
        f_wb = w * x[i] + b;
        dj_dw += (f_wb - y[i]) * x[i]
        dj_db += (f_wb - y[i])
        
    dj_dw /= m
    dj_db /= m
    return dj_dw, dj_db

# gradients descent
def gradient_descent(x, y, w_init, b_init, alpha, num_iters):
    w = w_init
    b = b_init
    cost_history = [] # track and analyze how the cost change during model
    # step down hill to local minima
    # keep decrease => learning rate good
    # stay flat => learning rate too small
    # explodes upward => learning rate too high
    
    for i in range(num_iters):
        dj_dw, dj_db = compute_gradients(x, y, w, b)
        w = w - alpha * dj_dw
        b = b - alpha * dj_db
        
        cost = compute_cost(x, y, w, b)
        print(f"cost history, {cost}")
        cost_history.append(cost)

        # just output value of parameters
        if i % 100 == 0 or i == num_iters - 1:
            print(f"Iteration {i}: Cost {cost:.2f}, w = {w:.2f}, b = {b:.2f}")
    
    return w, b, cost_history

# declare value
w_init = 0
b_init = 0
alpha = 0.01 # learning rate
iterations = 1000 # how much time for train

# run gradient descent
w_final, b_final, cost_hist = gradient_descent(x, y, w_init, b_init, alpha, iterations)

print(f"\nFinal_parameters: w = {w_final:.2f}, b = {b_final:.2f}")

# prediction
plt.plot(x, y, 'ro', label="training data")
plt.plot(x, w_final * x + b_final, label="prediction")
plt.xlabel("x (1000 sqft)")
plt.ylabel("y ($1000s)")
plt.legend()
plt.title("Linear Regression Fit")
plt.show()