import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 8)

software_dev = np.array([88, 84, 83, 90, 85, 80, 85])
marketing = np.array([66, 60, 65, 61, 60, 62, 62])
sales = np.array([54, 56, 58, 53, 55, 50, 55])
hr = np.array([32, 31, 34, 30, 33, 30, 32])
customer_support = np.array([75, 74, 76, 73, 70, 77, 72])

data = np.vstack([software_dev, marketing, sales, hr, customer_support])

fig, axs = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

total_productivity = data.sum(axis=0)
axs[0].plot(days, total_productivity, color='#2ca02c', linestyle='--', marker='s', linewidth=1.5, label='Total Productivity')
axs[0].fill_between(days, 0, total_productivity, color='#98df8a', alpha=0.6)
axs[0].set_xticks(days)
axs[0].grid(True, linestyle=':', linewidth=1)
axs[0].legend(loc='upper right')

# Stacked Area Chart for Daily Productivity by Department
axs[1].stackplot(days, data, 
                 colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.9)
axs[1].set_xticks(days)
axs[1].grid(True, linestyle=':', linewidth=1)

plt.tight_layout(rect=[0.02, 0.02, 0.98, 0.98])
plt.show()