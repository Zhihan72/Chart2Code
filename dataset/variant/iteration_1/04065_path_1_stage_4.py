import matplotlib.pyplot as plt
import numpy as np

# Define the periods and corresponding sales data
periods = ['Period 1', 'Period 2', 'Period 3', 'Period 4', 'Period 5', 
           'Period 6', 'Period 7', 'Period 8', 'Period 9', 'Period 10']
sales = np.array([60, 75, 90, 120, 130, 160, 170, 150, 135, 125])

# Combine periods and sales into a list of tuples for sorting
data = list(zip(periods, sales))

# Sort data by sales in descending order
data_sorted = sorted(data, key=lambda x: x[1], reverse=True)

# Separate periods and sales data after sorting
periods_sorted, sales_sorted = zip(*data_sorted)

# Create a bar chart
plt.figure(figsize=(14, 9))
plt.bar(periods_sorted, sales_sorted, color='skyblue', edgecolor='black')

plt.xlabel("Period", fontsize=14)
plt.ylabel("Cold Treats Sold (Units)", fontsize=14)
plt.title("Sales per Period in Descending Order", fontsize=16)

plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()

plt.show()