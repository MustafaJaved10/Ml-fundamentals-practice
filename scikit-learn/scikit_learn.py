# NumPy helps with arrays, Pandas helps with data,
# Matplotlib helps with graphs, and Scikit-learn helps
# build Machine Learning models.

# Scikit-learn is a Python library used for building, training, testing, and
# evaluating Machine Learning models.

# Scikit-learn is exactly like that.

# Instead of writing:

# gradient
# loss
# weight updates
# optimization

# you simply write:
# model.fit(X,y)

# from sklearn.linear_model import LinearRegression
# import numpy as np
# #    your model only nows y=mx +c so after seeing x it will predict eq itself
# X = np.array([[1],[2],[3],[4],[5],[6]])

# y = np.array([5,3,5,6,2,9])

# model = LinearRegression()
# # his creates an empty model.

# model.fit(X,y)  # learn weigth and bais


# print("Weight:", model.coef_)
# print("Bias:", model.intercept_)



# train and test

# Separate data into two parts: one part to teach the model and another
# part to check whether the model learned correctly on new unseen data.

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

# y = np.array([3,5,7,9,11,13,15,17,19,21])  # Your relationship is: y=2x+1 (output =y)

# x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42) #20% data → testing 80% data → training

# you always get the same split.  random_state  (give same pairs every time (x,y))
# It is used for reproducibility.

# Training data = 8 samples
# Testing data  = 2 samples
# print(x_train.shape, x_test.shape)


# X_train (Training Inputs)

# What it does:

# Contains input values given to the model during learning.
# The model looks at these X values and tries to find a relationship.


# y_train (Training Outputs)

# What it does:

# Contains the correct answers for X_train.
# The model compares its prediction with these answers and learns.

# X_train → Inputs used for learning
# y_train → Correct answers used for learning
# X_test → New inputs for checking
# y_test → Correct answers to evaluate model ✅(of x test )

# print("X_train:")
# print(x_train)

# print("X_test:")
# print(x_test)

# print("y_train:")
# print(y_train)

# print("y_test:")
# print(y_test)

# model = LinearRegression()

# model.fit(x_train, y_train)

# find y=wx+b
# Learned parameters

# print("\nWeight:", model.coef_)
# print("Bias:", model.intercept_)


# prediction = model.predict(x_test)  #ans of x test   prediction = Model's guesses

# The model does not see y_test.

# It only receives:

# model.predict(X_test)  and  apply this to find correct ans y=2x+1


# print("\nPredictions:")
# print(prediction)



# model.fit() trains the model, but train/test split decides which data the model
# is allowed to learn from and which data is kept hidden for testing

# Without train/test split: model see every data

# With train/test split:
# First divide data: train and test
# Training data teaches the model
# Testing data checks the model
# rain/test split separates data into learning data (X_train, y_train)
# for model.fit() and unseen data (X_test, y_test) to check whether the model learned correctly.
# y_test is compared with prediction.


# key points
# 1. X is the input (feature) and y is the correct output (target) from the original dataset.

# 2. train_test_split() divides the dataset into X_train, y_train (used for learning) and X_test, y_test (used for testing).

# 3. model.fit(X_train, y_train) trains the model by learning the best weight and bias from the training data.

# 4. model.predict(X_test) uses the learned weight and bias to predict outputs for the unseen X_test data.

# 5. Finally, prediction is compared with y_test to check how accurate the model's predictions are.


# X_train           y_train

# 1000   ------->   100000
# 1200   ------->   120000
# 1800   ------->   180000


# X_test            y_test

# 1500   ------->   150000
# 2000   ------->   200000


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = np.array([
    [100],
    [1200],
    [1500],
    [7500],
    [1250],
    [2400],
    [2600]
])

y = np.array([
    1000, 12000, 15000, 75000, 12500, 24000, 26000
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


print("weigth", model.coef_)
print("Bais", model.intercept_)

prediction = model.predict(X_test)
print("Prediction", prediction)
print("Actual value", y_test)


# loss=np.mean(error **2)  as we learn in LinearRegression

# using scikit it will be
# Smaller MSE = Better Model  mse is evalution metrics
mse = mean_squared_error(y_test, prediction)

print("Mean Squared Error:", mse)
