import matplotlib.pyplot as plt
import numpy as np

# Define the periods and corresponding sales data for two groups
periods = ['Period 1', 'Period 2', 'Period 3', 'Period 4', 'Period 5', 
           'Period 6', 'Period 7', 'Period 8', 'Period 9', 'Period 10']
sales_group_1 = np.array([60, 75, 90, 120, 130, 160, 170, 150, 135, 125])
sales_group_2 = np.array([50, 80, 100, 110, 120, 150, 165, 140, 130, 115])

# Combine periods and sales data into lists of tuples for sorting
data_group_1 = list(zip(periods, sales_group_1))
data_group_2 = list(zip(periods, sales_group_2))

# Sort data by sales in descending order for each group
data_sorted_1 = sorted(data_group_1, key=lambda x: x[1], reverse=True)
data_sorted_2 = sorted(data_group_2, key=lambda x: x[1], reverse=True)

# Separate periods and sales data after sorting for each group
periods_sorted_1, sales_sorted_1 = zip(*data_sorted_1)
periods_sorted_2, sales_sorted_2 = zip(*data_sorted_2)

# Create a bar chart for each group
plt.figure(figsize=(14, 9))

# Bar width
width = 0.4

# Create bars for the two groups with an offset
positions_1 = np.arange(len(periods))
positions_2 = positions_1 + width

plt.bar(positions_1, sales_sorted_1, width=width, color='skyblue', edgecolor='black', label='Group 1')
plt.bar(positions_2, sales_sorted_2, width=width, color='lightgreen', edgecolor='black', label='Group 2')

plt.xlabel("Period", fontsize=14)
plt.ylabel("Cold Treats Sold (Units)", fontsize=14)
plt.title("Sales per Period in Descending Order for Two Groups", fontsize=16)

plt.xticks(positions_1 + width / 2, periods_sorted_1, rotation=45, fontsize=12)
plt.yticks(fontsize=12)

plt.legend()

plt.tight_layout()

plt.show()