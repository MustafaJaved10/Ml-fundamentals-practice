# import numpy as np

# data=np.array([10,2,45,6,2,5,7,8])

# mean=np.mean(data)
# medain=np.median(data)

# std=np.std(data)

# var=np.var(data)

# print(f"Mean: {mean}")
# print(f"Medain {medain}")
# print(f"Std{std:.2f}")
# print(f"var {var:.2f}")

# import pandas as pd

# data=pd.Series([10,2,45,6,2,5,7,8])

# print(data.mode())

# print(data.value_counts())



# Statistics tells us what happened in data.
# Probability helps models make decisions when they are not completely sure.


# Probability measures how likely an event is, always a number between 0 and 1 (0 = impossible, 1 = certain).


# probality of getting number 6 on  dice

# total_outcome=6

# favorable_outcome=1

# prob=favorable_outcome / total_outcome

# print("Probaility:",prob)
# print("percentage",prob * 100 ,"%")

# What is the probability of getting Head?

# total_outcomes=2

# favorable_outcome=1

# prob=favorable_outcome / total_outcomes

# print(f"Probility of head  {prob}")
# print(f"Percentage of prob {prob *100}%")



# def probability(favourable,total):
#     return favourable/total


# print("probability:",probability(1,2))

# simulations

# The role of seed() is:

# It controls the starting point of random number generation so we can reproduce the same random results.
# till we reach 10000 sequence of num will same

import numpy as np

# np.random.seed(1)

# rolls=np.random.randint(1,7,size=10000)

# prob_3=np.sum(rolls==3)/len(rolls)

# print(prob_3)


# independent prob (One event does not affect the other event.)
# find

# p_head=1/2
# p_6=1/6

# independent= p_head * p_6

# print(independent)


# check independent or not

# p_head=0.5
# p_6=0.2

# p_h_and_p_6=0.1

# if p_h_and_p_6 == p_head * p_6 :
#     print("Independent ")
# else :
#     print("Not independent ")

# P(A∩B)=0.3333  ( and)

# P(A)×P(B)=0.33335  (*)

# Difference:

# ∣0.3333−0.33335∣
# =0.00005

# Now compare:

# 0.00005<0.001  so independent

import pandas as pd

# data={
#     "weather" : ["sunny","sunny","rain","rain","sunny","rain"],
#     "play"   : ["yes","No","yes","No","yes","yes"]

# }
# df=pd.DataFrame(data)

# total=len(df)

# p_sunny=len(df[df["weather"]== "sunny"]) / total

# p_yes=len(df[df["play"]=="yes"]) / total

# p_no=len (df[df["play"]=="No"])  / total


# p_suuny_and_yes= len (   df [ (df["weather"]== "sunny")  &  (df["play"]=="yes")]  )  / total

# p_suuny_and_no  = len ( df [(df ["weather"]== "sunny")   & (df["play"]=="No")   ])  / total



# calculated= p_sunny  * p_yes

# print(p_sunny)
# print(p_yes)
# print(p_no)
# print(p_suuny_and_yes)
# print(p_suuny_and_no)
# print(calculated)

# if abs(p_suuny_and_yes - calculated) < 0.001:   #abs no neg output
#     print("independent ")
# else :
#     print("dependent")

# conditional

# The probability of an event when we already know that another event has happened.

# Formula
# P(A∣B)=P(A∩B) / p(B)


# students = 100

# students_play_cricket = 20

# total_students = 40


# conditional_probability = students_play_cricket / total_students


# print(conditional_probability)



# data={
#     "weather" : ["sunny","sunny","rain","rain","sunny","rain"],
#     "play"   : ["yes","No","yes","No","yes","yes"]

# }
# df=pd.DataFrame(data)

# total=len(df)

# p_sunny=len(df[df["weather"]=="sunny"]) / total

# p_suuny_and_yes= len (   df [ (df["weather"]== "sunny")  &  (df["play"]=="yes")]  )  / total

# result=p_suuny_and_yes / p_sunny

# print(result)


# dice=np.array([1,2,3,4,5,6])

# num_G_3= dice[dice>3]

# even_D_3=num_G_3[num_G_3 % 2==0]

# result=len(even_D_3)/ len(num_G_3)

# print(result)


# # Step 1: Find B (given condition)

# B = len(df[df["column"] == condition])


# # Step 2: Find A and B together

# A_and_B = len(
#     df[
#         (df["column1"] == condition1) &
#         (df["column2"] == condition2)
#     ]
# )


# # Step 3: Conditional probability

# answer = A_and_B / B


# Bayes' Theorem (core formula, used in Naive Bayes classifier)
# P(A|B) = ( P(B|A) * P(A) ) / P(B)
# Bayes' Theorem tells us how to update our belief about something after receiving new information.

# Bayes theorem example

# p_disease = 0.1

# p_positive_given_disease = 0.9

# p_positive = 0.18


# p_disease_given_positive = (
#     p_positive_given_disease * p_disease
# ) / p_positive


# print(p_disease_given_positive)


# Bayes Theorem - Disease Test Example


# # Prior probability
# p_disease = 0.01


# # Probability of positive test if disease exists
# p_positive_given_disease = 0.99


# # Probability of positive test if no disease exists
# p_positive_given_no_disease = 0.05


# # Probability of no disease
# p_no_disease = 1 - p_disease


# # Total probability of positive test
# p_positive = (
#     (p_positive_given_disease * p_disease)
#     +
#     (p_positive_given_no_disease * p_no_disease)
# )


# # Bayes theorem
# p_disease_given_positive = (
#     (p_positive_given_disease * p_disease)
#     /
#     p_positive
# )


# print("Probability of disease given positive test:",
#       p_disease_given_positive)


# A spam filter knows that 20% of emails are spam.
# 80% of spam emails contain the word "free", while only 10% of normal emails contain this word.
# If an email contains the word "free", what is the probability that it is spam?

# Bayes Theorem - Spam Example


# # Prior probability
# p_spam = 0.20
# p_not_spam = 0.80


# # Likelihood
# p_free_given_spam = 0.80
# p_free_given_not_spam = 0.10


# # Total probability of seeing "free"
# p_free = (
#     (p_free_given_spam * p_spam)
#     +
#     (p_free_given_not_spam * p_not_spam)
# )


# # Bayes theorem
# p_spam_given_free = (
#     (p_free_given_spam * p_spam)
#     /
#     p_free
# )


# print("P(Free):", p_free)
# print("P(Spam | Free):", p_spam_given_free)


# spam=0.3
# n_spam=0.7

# offer_spam=0.60

# offer_n_spma=0.10

# offer=(spam * offer_spam) + (n_spam * offer_n_spma)

# result=(offer_spam * spam)  / offer

# print(result)

# . We know the probability in one direction but need the opposite direction.
# If email is spam, how likely it contains "free".
# If email contains "free", what is the chance it is spam


# Normal Distribution (the bell curve)

# Normal Distribution is a probability distribution where most data points are
# close to the average (mean), and fewer data points are far away from the average.


# Standard deviation tells:
# How spread out the data is from the mean.


import matplotlib.pyplot as plt
import numpy as np


marks = np.random.normal(
    loc=70,      # mean(nums mostly near it )
    scale=10,    # diff (70 to 80 or 70 to 60 ,10 ,20 ,then 30)
    size=1000    # total numbs
)


plt.hist(
    marks,
    bins=30
)

plt.show()
