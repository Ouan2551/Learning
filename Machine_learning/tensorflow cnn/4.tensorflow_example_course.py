import numpy as np
import tensorflow.compat.v1 as tf #type: ignore
tf.disable_v2_behavior() # run old version of tensorflow version 1.x not 2.x

coefficients = np.array([[1.], [-20.], [100.]])

# define parameters
w = tf.Variable(0,dtype=tf.float32)
x = tf.placeholder(tf.float32, [3,1]) # training data
# cost = tf.add(tf.add(w**2,tf.multiply(-10., w)),25)
# cost =  w**2 - 10*w + 25
cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost) # can change to another optimizer

init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)
print(session.run(w))

session.run(train, feed_dict={x:coefficients}) # run 1 step of gradient descend
print(session.run(w))

for i in range(1000):
    session.run(train, feed_dict={x:coefficients})
print(session.run(w))