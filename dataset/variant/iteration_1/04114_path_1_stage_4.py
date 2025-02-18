import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
rainfall = np.array([85, 78, 92, 110, 134, 158, 102, 75, 65, 45, 40, 70])

sorted_indices = np.argsort(rainfall)
sorted_rainfall = rainfall[sorted_indices]
sorted_month_labels = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])[sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(sorted_month_labels, sorted_rainfall, color='lightcoral', edgecolor='darkred', hatch='/')

# Adding data labels with different angle for variety
for bar in ax.containers[0]:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(-10, 3), textcoords='offset points', rotation=45, ha='center', fontsize=12, color='navy')

# Title and labels with changed styles and positions
ax.set_title("Monthly Rainfall (mm)", fontsize=18, fontweight='heavy', pad=20, color='darkgreen')
ax.set_xlabel("Month", fontsize=14, style='italic', color='teal')
ax.set_ylabel("Rainfall (mm)", fontsize=14, style='italic', color='teal')

# Modified grid lines and line style
ax.grid(axis='y', color='gray', linestyle='-.', linewidth=1, alpha=0.8)

# Add borders
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

plt.tight_layout()
plt.show()