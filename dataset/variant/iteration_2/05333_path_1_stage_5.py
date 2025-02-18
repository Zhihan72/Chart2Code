import matplotlib.pyplot as plt
import numpy as np

# Campaigns and their corresponding total sales arrays
campaigns = ['Social Media', 'TV Ads', 'Email Marketing', 'Billboards', 'Trade Shows']

Q1_sales = np.array([12000, 25000, 15000, 18000, 20000])
Q2_sales = np.array([13000, 26000, 16000, 21000, 19000])
Q3_sales = np.array([22000, 17000, 14000, 27000, 20000])
Q4_sales = np.array([23000, 28000, 21000, 15000, 18000])

# Calculating total sales for each campaign
total_sales = Q1_sales + Q2_sales + Q3_sales + Q4_sales

# Sorting indices based on total sales in ascending order
sorted_indices = np.argsort(total_sales)

# Reordering all arrays based on the sorted indices
campaigns = [campaigns[i] for i in sorted_indices]
Q1_sales = Q1_sales[sorted_indices]
Q2_sales = Q2_sales[sorted_indices]
Q3_sales = Q3_sales[sorted_indices]
Q4_sales = Q4_sales[sorted_indices]
total_sales = total_sales[sorted_indices]

# Define the colors for each campaign
colors_campaigns = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.2
positions = np.arange(len(campaigns))

# Plot the bar for each quarter sorted by total sales
ax.bar(positions - 1.5*bar_width, Q1_sales, width=bar_width, color=colors_campaigns, edgecolor='black')
ax.bar(positions - 0.5*bar_width, Q2_sales, width=bar_width, color=colors_campaigns, edgecolor='black', alpha=0.9)
ax.bar(positions + 0.5*bar_width, Q3_sales, width=bar_width, color=colors_campaigns, edgecolor='black', alpha=0.8)
ax.bar(positions + 1.5*bar_width, Q4_sales, width=bar_width, color=colors_campaigns, edgecolor='black', alpha=0.7)

# Optional: Plot total sales as a line
ax.plot(positions, total_sales, color='purple', marker='o', linestyle='-', linewidth=2, markersize=8)

ax.set_xticks(positions)
ax.set_xticklabels(campaigns)
plt.tight_layout()
plt.show()