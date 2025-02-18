import matplotlib.pyplot as plt
import numpy as np

# Prepare data
food_delivery_data = [np.array([3, 4, 3.5, 4, 5]), np.array([5, 4.5, 5, 4.8, 5.0]), 
                     np.array([7, 6.8, 7.2, 7, 6.5]), np.array([9, 8.5, 9.5, 9, 9.3]),
                     np.array([12, 11.5, 12.5, 11.8, 12.2])]
online_retail_data = [np.array([15, 14, 16, 15.5, 14.8]), np.array([25, 24.5, 24.8, 25.3, 25.0]),
                     np.array([35, 34.8, 35.2, 33.8, 35]), np.array([45, 44, 46, 45.8, 44.2]),
                     np.array([60, 59.5, 60.2, 58, 59.8])]

ecommerce_data = list(zip(food_delivery_data, online_retail_data))

# Create horizontal box plot
fig, ax1 = plt.subplots(figsize=(14, 8))
boxprops = dict(linestyle='-', linewidth=2, color='midnightblue')
flierprops = dict(marker='o', color='red', alpha=0.5)

for index, (fd_data, or_data) in enumerate(ecommerce_data):
    ax1.boxplot(fd_data, positions=[index*2], widths=0.6, vert=False, boxprops=boxprops, flierprops=flierprops)
    ax1.boxplot(or_data, positions=[index*2+1], widths=0.6, vert=False, boxprops=boxprops, flierprops=flierprops)

ax1.set_yticks(np.arange(0, 10, 2) + 0.5)

ax1.grid(linestyle='-', alpha=0.3)
plt.tight_layout()
plt.show()