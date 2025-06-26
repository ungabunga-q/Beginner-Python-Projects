"""
Data Visualization: Plotting with Matplotlib
--------------------------------------------
Plots a simple line graph from a list of numbers.

Steps for Beginners:
1. Import matplotlib.pyplot for plotting.
2. Create a list of numbers to plot.
3. Use plt.plot() to create a line graph.
4. Show the plot with plt.show().
"""

# 1. Import matplotlib
import matplotlib.pyplot as plt

# 2. Data to plot
data = [1, 3, 2, 5, 7, 4, 6]

# 3. Plot the data
plt.plot(data)
plt.title("Simple Line Plot")
plt.xlabel("Index")
plt.ylabel("Value")

# 4. Show the plot
plt.show()
