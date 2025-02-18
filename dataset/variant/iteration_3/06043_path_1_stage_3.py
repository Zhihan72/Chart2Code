import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 8)

software_dev = np.array([80, 85, 83, 90, 88, 85, 84])
marketing = np.array([60, 62, 61, 65, 66, 62, 60])
sales = np.array([50, 55, 53, 58, 56, 54, 55])
hr = np.array([30, 32, 31, 34, 33, 32, 30])
customer_support = np.array([70, 72, 75, 77, 76, 74, 73])

data = np.vstack([software_dev, marketing, sales, hr, customer_support])

fig, axs = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# Line Plot for Total Productivity
total_productivity = data.sum(axis=0)
axs[0].plot(days, total_productivity, color='#d62728', linestyle='-', marker='o', linewidth=2)
axs[0].fill_between(days, 0, total_productivity, color='#ff9896', alpha=0.5)
axs[0].set_xticks(days)
axs[0].grid(True, linestyle='--', linewidth=0.5)

# Stacked Area Chart for Daily Productivity by Department
axs[1].stackplot(days, data, 
                 colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.8)
axs[1].set_xticks(days)
axs[1].grid(True, linestyle='--', linewidth=0.5)

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()