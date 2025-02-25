import matplotlib.pyplot as plt
import numpy as np

# Adjusting the data to suit a diverging bar chart
# Group two sets of data representing positive and negative sales
positive_sales = np.array([
    [150, 200, 300, 400, 450, 500, 550, 600, 700, 750, 800, 850],
    [90, 110, 150, 180, 200, 250, 260, 300, 330, 350, 365, 380]
])

negative_sales = np.array([
    [-100, -140, -160, -200, -220, -260, -270, -320, -340, -360, -380, -400],
    [-80, -120, -150, -200, -210, -260, -300, -330, -370, -400, -430, -460]
])

colors_positive = ['#4B0082', '#9370DB']
colors_negative = ['#FF6347', '#FFD700']

fig, ax = plt.subplots(figsize=(14, 8))
index = np.arange(12)

# Plotting positive bars
for i in range(len(positive_sales)):
    if i == 0:
        ax.bar(index, positive_sales[i], 0.7, color=colors_positive[i])
    else:
        ax.bar(index, positive_sales[i], 0.7, bottom=np.sum(positive_sales[:i], axis=0), color=colors_positive[i])

# Plotting negative bars
for i in range(len(negative_sales)):
    if i == 0:
        ax.bar(index, negative_sales[i], 0.7, color=colors_negative[i])
    else:
        ax.bar(index, negative_sales[i], 0.7, bottom=np.sum(negative_sales[:i], axis=0), color=colors_negative[i])

ax.axhline(0, color='black', linewidth=0.8)
plt.show()