# -*- coding: utf-8 -*-
"""A_53_ML_7_XOR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e040miYyEfuDL8L5J7VmNlnpdQEt-HHe
"""

import numpy as np

def sigmoid(x):
  return 1/(1+np.exp(-x))

def derivative_sigmoid(x):
  return x*(1-x)

X = np.array([[0,0], [0,1], [1,0], [1,1]])
Y = np.array([[0],[1],[1],[0]])

input_size = 2
hidden_size = 4
output_size = 1
learning_rate = 0.1

# INIT WEIGHTS & BIAS

np.random.seed(42)

weights_of_input_hidden = np.random.uniform(size = (input_size, hidden_size))
bias_of_hidden = np.zeros((1, hidden_size))

weights_of_output_hidden = np.random.uniform(size = (hidden_size, output_size))
bias_of_output = np.zeros((1, output_size))

#  training neural network
EPOCHS = 10000


for epoch in range(EPOCHS):

  # FORWARD PROPOGATION
  input_for_hidden = np.dot(X, weights_of_input_hidden) + bias_of_hidden
  output_for_hidden = sigmoid(input_for_hidden)

  input_for_last_layer = np.dot(output_for_hidden, weights_of_output_hidden) + bias_of_output
  calculated_output = sigmoid(input_for_last_layer)




  # error
  error = Y - calculated_output

  # BACKWARD PROPOGATION
  delta_for_output = error * derivative_sigmoid(calculated_output)

  error_hidden_layer = delta_for_output.dot(weights_of_output_hidden.T)
  delta_for_hidden_layer = error_hidden_layer * derivative_sigmoid(output_for_hidden)




  # UPDATE WEIGHTS AND BIAS
  weights_of_output_hidden += output_for_hidden.T.dot(delta_for_output) * learning_rate
  weights_of_input_hidden += X.T.dot(delta_for_hidden_layer) * learning_rate

  bias_of_output += np.sum(delta_for_output, axis=0, keepdims=True) * learning_rate
  bias_of_hidden += np.sum(delta_for_hidden_layer, axis=0, keepdims=True) * learning_rate

  # display error at certain intervals
  if epoch % 1000 == 0:
    mean_error = np.mean(np.abs(error))
    print("Error : ", mean_error)
    # print("Error : ", error)

print(weights_of_input_hidden)
print(weights_of_output_hidden)

# Testing
test_input = np.array([[0,0], [0,1], [1,0], [1,1]])

test_hidden_layer_input = np.dot(test_input, weights_of_input_hidden) + bias_of_hidden
test_hidden_layer_output = sigmoid(test_hidden_layer_input)

test_output_layer_input = np.dot(test_hidden_layer_output, weights_of_output_hidden) + bias_of_output
test_output_layer_output = sigmoid(test_output_layer_input)

print(test_output_layer_output, end="\n\n\n")
print(np.round(test_output_layer_output))

