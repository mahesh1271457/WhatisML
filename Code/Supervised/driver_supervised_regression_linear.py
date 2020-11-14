# driver_supervised_linearregression.py

import example_regression
import matplotlib.pyplot as plt
import NeuralNetwork
import numpy as np
import Optimizer
import plot_results

# Things to try:
# Change random seed to get different random numbers: seed
# Change number of data samples: nsample
# Change learning rate for optimization: learning_rate
# Change number of iterations: niterations
seed = 100
nsample = 500
learning_rate = 0.1
niterations = 100
# (1) Set up data
nfeature = 1
X,Y = example_regression.example(nfeature,nsample)
# (2) define model
model = NeuralNetwork.NeuralNetwork(nfeature)
model.add_layer(1,"linear")
# set initial guess for W and b
initial_param = [{"W": -0.2, "b":1.4}]
model.set_param(initial_param)
# (3) define loss function and optimizer
optimizer = Optimizer.GradientDescent(learning_rate)
model.compile("meansquarederror",optimizer)
# (4) Learning
history = model.fit(X,Y,niterations)
# (5) Results
# plot loss 
plot_results.plot_results_history(history,["loss"])
# plot data and final machine learning solution
plot_results.plot_results_linear(X,Y,model=model)
# animation
plot_results.plot_results_linear_animation(X,Y,model)
plt.show()