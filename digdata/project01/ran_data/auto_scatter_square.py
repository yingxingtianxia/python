import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolors='none', c='red', s=10)
plt.title("Squares Values", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axes([1, 1000, 0, 1100000])
plt.show()