# import sys
# import matplotlib
# matplotlib.use('Agg')


import matplotlib.pyplot as plt
import numpy as np

# pyplot is a tool inside whole libariry mathplotlib use for making of graphs easily
# module

# import numpy as np

# x=np.array[0,6]
# y=np.array[10,50]

# plt.points(x,y)
# plt.show()

# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()



# x=[1,2,3,4,5]
# y=[7,8,9,10,11]

# plt.plot(x, y)

# plt.title("Simple Line Plot")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.show()

# x=np.array([1,8])
# y=np.array([7,14])

# plt.plot(x,y)
# plt.title("My Math")
# plt.xlabel("X axis ")
# plt.ylabel("Y axis ")
# plt.show()



# x=np.array([1,8])
# y=np.array([7,14])

# plt.plot(x,y,'o')   print withoutline
# plt.title("My Math")
# plt.xlabel("X axis ")
# plt.ylabel("Y axis ")
# plt.show()

# Multiple points
# xpoints = np.array([1,2,6,8])
# ypoints = np.array([3,8,1,7])

# plt.plot(xpoints, ypoints)
# plt.show()


# x points as default
# ypoints = np.array([3,8,1,7])

# plt.plot(ypoints)
# plt.show()

# marker at each point
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o')
# plt.show()

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, linestyle = 'dotted')
# plt.show()


# color

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, color = 'r')
# plt.show()


# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, linewidth = '20.5')
# plt.show()


# x=np.array([1,7,9,2])
# y=np.array([5,2,9,1])

# plt.plot(x)
# plt.plot(y)

# plt.show()


# x = np.linspace(0, 10, 50)  #strt ,stop,total values
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, label="sin(x)", color="blue")
# plt.plot(x, y2, label="cos(x)", color="red", linestyle="--")

# plt.title("Sine vs Cosine")
# plt.xlabel("x")    #give line name
# plt.ylabel("value")
# plt.legend()  #box tell which line represnt wht
# plt.show()


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}

# plt.title("Sports Watch Data", fontdict = font1)  fontdict chnge style
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)

# plt.plot(x, y)
# plt.grid()   add grid

# plt.grid(axis = 'x')  only x grid will display


# plt.show()


# side alignment
# plt.title("Sports Watch Data", loc = 'left')

# sub plot

# plt.subplot(rows, columns, index)  syntx

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)


# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)

# plt.suptitle("MY SHOP")
# plt.show()



# Bars

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x,y)
# plt.show()


# categories = ["Lahore", "Karachi", "Multan", "Islamabad"]
# values = [50000, 65000, 40000, 58000]

# plt.bar(categories, values, color="green")
# plt.title("Average Salary by City")
# plt.xlabel("City")
# plt.ylabel("Salary")

# # plt.barh(x, y) horizontal bar
# plt.show()

# scatter

# age = [22, 25, 21, 23, 28, 24, 26]
# salary = [40000, 55000, 38000, 45000, 62000, 47000, 58000]

# plt.scatter(age, salary, color="purple")
# plt.title("Age vs Salary")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.show()


# histogram

# x = np.random.normal(170, 10, 250) (mean, standard_deviation, size)

# plt.hist(x)
# plt.show()

# pie chart

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels, startangle = 90)
# plt.show()


# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]

# # plt.pie(y, labels = mylabels, explode = myexplode)  diffr the paprmeter apple
# plt.show()



# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels)
# plt.legend(title = "Four Fruits:")   small box fr understanding
# plt.show()

import pandas as pd

df = pd.DataFrame({
    "city": ["Lahore", "Karachi", "Lahore", "Multan", "Karachi"],
    "salary": [50000, 60000, 55000, 40000, 65000]
})

avg_salary = df.groupby("city")["salary"].mean()

avg_salary.plot(kind="bar", color="teal", title="Average Salary by City")
plt.ylabel("Salary")
plt.show()
