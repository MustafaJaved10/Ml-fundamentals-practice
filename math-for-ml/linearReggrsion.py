# Linear Regression learns the best-fitting straight-line equation between
# an input (X) and an output (Y) so it can predict continuous values.


#  Training Data
#       ↓
# Find best line
#       ↓
# Learn m and b
#       ↓
# Use equation
#       ↓
# Predict new values

# y=mx + b

# y is output ,x is given ,m is slope (weigth) and b is intercept or bais (starting point) -> diff

# Given
# x = 10
# y = 100

# # Initial values
# weight = 5
# bias = 0

# learning_rate = 0.001

# for i in range(10):

#     # Prediction
#     prediction = (weight * x) + bias

#     # Loss  for 1 sample
#     loss = (y - prediction) ** 2
#     #  more than 1 sample
#     # loss = np.mean((actual - prediction) ** 2)

#     # Gradient for weight  comes after taking derivate of loss
#     gradient_weight = -2 * x * (y - prediction)

#     # Gradient for bias
#     gradient_bias = -2 * (y - prediction)

#     print(
#         "i:", i,
#         "weight:", weight,
#         "bias:", bias,
#         "prediction:", prediction,
#         "loss:", loss
#     )

#     # Update weight
#     weight = weight - learning_rate * gradient_weight

#     # Update bias
#     bias = bias - learning_rate * gradient_bias


# print("\nFinal Weight:", weight)
# print("Final Bias:", bias)

# y=mx + b

import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([5, 3, 5, 6, 2, 9])

weight = 0
bais = 0

learning_rate = 0.01

n = len(x)

for i in range(10):
    prediction = weight * x + bais

    error = y - prediction  # for single data

    loss = np.mean(error ** 2)

    gradient = (-2 / n) * np.sum(x * error)
    gradient_bias = (-2 / n) * np.sum(error)

    print(
        "i:", i,
        "weight:", weight,
        "bias:", bais,
        "prediction:", prediction,
        "error:", error,
        "loss:", loss
    )
    weight = weight - learning_rate * gradient
    bais = bais - learning_rate * gradient_bias


print("Final weight", weight)
print("final Bais ", bais)


# New Prediction
# For x=1:
# prediction=0.38(1)+0.1
# =0.48
# For x=2:
# prediction=0.38(2)+0.1
# =0.86
# For x=3:
# prediction=0.38(3)+0.1
# =1.24
