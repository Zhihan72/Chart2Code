import matplotlib.pyplot as plt
import numpy as np

# Branches : 'Downtown', 'Uptown', 'Suburb', 'Airport', 'University', 'Mall'
branches = ['Downtown', 'Uptown', 'Suburb', 'Airport', 'University', 'Mall']
months = np.arange(1, 13)

# Coffee consumption data in kilograms for each branch
downtown_consumption = [240, 200, 210, 220, 230, 240, 245, 250, 240, 230, 220, 215]
uptown_consumption = [180, 190, 200, 195, 205, 200, 205, 210, 200, 190, 185, 195]
suburb_consumption = [150, 145, 140, 150, 155, 160, 165, 170, 165, 160, 155, 150]
airport_consumption = [300, 310, 320, 300, 290, 280, 285, 290, 295, 300, 310, 320]
university_consumption = [100, 110, 120, 115, 125, 130, 135, 140, 130, 120, 110, 105]
mall_consumption = [220, 225, 230, 235, 220, 210, 215, 225, 230, 235, 240, 245]

# Creating the subplots
fig, axes = plt.subplots(2, 1, figsize=(14,12), constrained_layout=True)

# Plot 1: Bar chart for coffee consumption per branch across months
bar_width = 0.12
x_indices = np.arange(len(months))

for i, (consumption, label) in enumerate(zip([downtown_consumption, uptown_consumption, suburb_consumption, airport_consumption, university_consumption, mall_consumption], branches)):
    axes[0].bar(x_indices + i * bar_width, consumption, bar_width, label=label)

# Beautifying the plot
axes[0].set_title("Monthly Coffee Consumption Across Different Branches (2022)", fontsize=16, fontweight='bold', pad=20)
axes[0].set_xlabel("Month", fontsize=14)
axes[0].set_ylabel("Coffee Consumption (kg)", fontsize=14)
axes[0].set_xticks(x_indices + bar_width * (len(branches) - 1) / 2)
axes[0].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45, ha='right')
axes[0].legend(loc='upper left', title='Branches', fontsize=12)
axes[0].grid(True, linestyle='--', alpha=0.7)

# Plot 2: Grouped bar chart to compare average consumption per branch during quarters
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
x_indices_2 = np.arange(len(quarters))
average_consumptions = {
    'Downtown': [np.mean(downtown_consumption[i*3:i*3+3]) for i in range(4)],
    'Uptown': [np.mean(uptown_consumption[i*3:i*3+3]) for i in range(4)],
    'Suburb': [np.mean(suburb_consumption[i*3:i*3+3]) for i in range(4)],
    'Airport': [np.mean(airport_consumption[i*3:i*3+3]) for i in range(4)],
    'University': [np.mean(university_consumption[i*3:i*3+3]) for i in range(4)],
    'Mall': [np.mean(mall_consumption[i*3:i*3+3]) for i in range(4)],
}

for i, (label, avg) in enumerate(average_consumptions.items()):
    axes[1].bar(x_indices_2 + i * bar_width, avg, bar_width, label=label)

# Beautifying the plot
axes[1].set_title("Average Quarterly Coffee Consumption Comparison (2022)", fontsize=16, fontweight='bold', pad=20)
axes[1].set_xlabel("Quarter", fontsize=14)
axes[1].set_ylabel("Average Coffee Consumption (kg)", fontsize=14)
axes[1].set_xticks(x_indices_2 + bar_width * (len(branches) - 1) / 2)
axes[1].set_xticklabels(quarters, rotation=45, ha='right')
axes[1].legend(loc='upper left', title='Branches', fontsize=12)
axes[1].grid(True, linestyle='--', alpha=0.7)

plt.show()