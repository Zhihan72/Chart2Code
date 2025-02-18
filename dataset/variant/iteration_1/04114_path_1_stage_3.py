import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
rainfall = np.array([85, 78, 92, 110, 134, 158, 102, 75, 65, 45, 40, 70])

sorted_indices = np.argsort(rainfall)
sorted_rainfall = rainfall[sorted_indices]
sorted_month_labels = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])[sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(sorted_month_labels, sorted_rainfall, color='skyblue', edgecolor='black')

for bar in ax.containers[0]:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3), textcoords='offset points', ha='center', fontsize=10, color='black')

ax.set_title("Monthly Rainfall (mm)", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Rainfall (mm)", fontsize=12)

ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()