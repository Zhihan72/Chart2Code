import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2018, 2019, 2020, 2021, 2022])
stores = ["A", "B", "C", "D", "E"]
revenue = np.array([
    [15, 10, 11, 12, 14],
    [10, 8, 13, 12, 9],
    [20, 15, 14, 18, 16],
    [17, 16, 15, 13, 14],
    [14, 12, 9, 10, 13],
])

# Calculate total revenue for sorting
total_revenue = revenue.sum(axis=1)
sorted_indices = np.argsort(-total_revenue)  # Sort in descending order

# Sort stores and revenue based on total revenue
sorted_stores = np.array(stores)[sorted_indices]
sorted_revenue = revenue[sorted_indices]

# Plot sorted bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
x = np.arange(len(stores))

# Sum revenue across years for each store for a simple bar plot
ax.bar(x, total_revenue[sorted_indices], color='#1f77b4', alpha=0.7)

# Set labels and title
ax.set_title('Stores: Sorted by Total Revenue (2018-2022)', fontsize=14, fontweight='bold')
ax.set_xlabel('Store', fontsize=12)
ax.set_ylabel('Total Revenue (M)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(sorted_stores)

plt.tight_layout()
plt.show()