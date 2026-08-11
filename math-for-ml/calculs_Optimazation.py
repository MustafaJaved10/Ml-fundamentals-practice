# actual and predict difference is fond and goal is to minimize and end the diff
# calculs -> derivatie -> how much loss changes (difference ) when prameter changes

# parmeter increse check loss (increase or decrease)
# parmater decrease loss (inc or dec )

# if we konw der then we can tell that we have to increase or decrese Bete (paramter )

# 1 direction (inc or dec by deri)

# optimization during learing phase (how far to move )

# 2 use gradients to update parameters



# def f(x):
#     return x**2

# x = 2      # Point where we want the derivative
# h = 0.1    # Small change

# derivative = (f(x + h) - f(x)) / h

# print("Approximate Derivative:", derivative)



# derivate of x3 and put x=2

# def derivative(x):
#     return 3 * x**2

# print(derivative(4))



# not now derivate in advance  (numerical derivate

# x 5 derivarte

# def f(x):
#     return x**5

# x=2
# h=0.0001

# derivative = (f(x+h) - f(x)) / h

# print(derivative)

#   differnet h


# h means a small change in the input value x.
# x → current position
# h → small step forward


# def f(x):
#     return x**2

# x=2

# for h in [1,0.1,0.01,0.001,0.0001]:
#     derivate= (f(x+h) - f(x))  /h
#     print(h,derivate)



# x square and y square

# def f(x,y):
#     return x**2 + y**2

# x=2
# y=3

# for h in [1,0.1,0.01,0.001,0.0001]:
#     dx=(f(x+h,y) - f(x,y))/h
#     dy=(f(x,y+h)- f(x,y)) /h
#     print(h,dx)
#     print(h,dy)


# central differnece derivate way

# looks both forward and behind both way ,more coorect

# x square

# def f(x):
#     return x**2


# def central_difference(f, x, h):
#     return (f(x+h) - f(x-h)) / (2*h)


# print(central_difference(f, 3, 0.1))



# def f(x):
#     return x **5

# def central(f,x,h):
#     return (f(x+h) - f(x-h))  / (2*h)


# print(central)

# weigth and loss ,weigth changes ,how does loss changes

# def loss(w):
#     return w **2

# def central(loss,w,h=0.0001):
#        return (loss(w+h) - loss(w-h)) / (2*h)
# weigth=3

# gradeint=central(loss,weigth)

# print("Gradient:",gradeint)

# print("central difference",central)

    # during training
# A weight is a value that the model can change to improve its output.

# The gradient answers:

# "If I increase the weight a little, does my result become better or worse?"

# Gradient tells us which direction and how much we should change
# our weights to reduce the loss.
# Loss tells us how close or far we are from the correct result.

# during answering(prediction)

# loss calculation ❌
# Gradient calculation ❌
# Weight update ❌

# Because it is not learning anymore.


# size = 1000
# actual_price = 100000

# weight = 50

# learning_rate = 1e-8


# for epoch in range(20):

#     # Prediction
#     prediction = size * weight

#     # Loss
#     loss = (actual_price - prediction) ** 2

#     # Gradient
#     gradient = -2 * size * (actual_price - prediction)

#     # Weight update
#     weight = weight - learning_rate * gradient

#     print(
#         "Epoch:", epoch,
#         "Weight:", weight,
#         "Prediction:", prediction,
#         "Loss:", loss
#     )


# print("Final Weight:", weight)

# Model -> prediction =size * weigth

# p=xw, x is input ,w is model paramter

# loss we use Mean squared error =(actual - prediction) sqaure
# l=y-p

# l=y-xw ,square  so its derivate is −2x(y−xw)


# size = 10
# actual_price = 100

# weight = 5

# learning_rate = 0.01


# for epoch in range(10):

#     # 1. Prediction
#     prediction = size * weight

#     # 2. Loss
#     loss = (actual_price - prediction) ** 2

#     # 3. Gradient
#     gradient = -2 * size * (actual_price - prediction)

#     # 4. Update weight
#     weight = weight - learning_rate * gradient

#     print(
#         "Epoch:", epoch,
#         "Weight:", round(weight,2),
#         "Prediction:", round(prediction,2),
#         "Loss:", round(loss,2)
#     )


# print("Final Weight:", round(weight,2))



# Gradient tells us the direction and amount of change needed to reduce the loss.

# Gradient Descent is the algorithm that uses the gradient to update the weights.


# New Weight=Old Weight−LearningRate×Gradient


# 1. Calculate Gradient
#         ↓
# 2. Use Gradient inside Gradient Descent
#         ↓
# 3. Update Weight



# prediction of weigth for model given size and price
# training
size = 10
price = 100

# inital
weigth = 5

learning_rate = 0.001

for i in range(10):
    prediction = size * weigth

    loss = (price - prediction) ** 2

    gradient = -2 * size * (price - prediction)

    print(
        "i:", i,
        "weigth:", weigth,
        "prediction:", prediction,
        "gradient:", gradient,
        "loss", loss
    )
    weigth = weigth - learning_rate * gradient

print("final weigth:", weigth)
