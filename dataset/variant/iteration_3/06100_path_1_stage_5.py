import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June']
north_sales = [22, 15, 30, 25, 35, 20]
south_sales = [12, 28, 10, 20, 15, 25]
east_sales = [35, 18, 40, 30, 22, 27]
west_sales = [15, 8, 18, 22, 12, 10]

colors = ['#FF5733', '#28A745', '#007ACC', '#FFD700']

fig, ax = plt.subplots(figsize=(10, 7))

bar_height = 0.2
index = np.arange(len(months))

ax.barh(index - bar_height*1.5, north_sales, bar_height, color=colors[0])
ax.barh(index - bar_height/2, south_sales, bar_height, color=colors[1])
ax.barh(index + bar_height/2, east_sales, bar_height, color=colors[2])
ax.barh(index + bar_height*1.5, west_sales, bar_height, color=colors[3])

ax.set_yticks(index)
ax.set_yticklabels(months)

plt.tight_layout()
plt.show()