import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
rainfall = np.array([85, 78, 92, 110, 134, 158, 102, 75, 65, 45, 40, 70])

season_colors = ['skyblue', 'lightgreen', 'gold', 'coral']

fig, ax = plt.subplots(figsize=(14, 8))

colors = [season_colors[(month - 1) // 3] for month in months]
bars = ax.bar(months, rainfall, color=colors, edgecolor='black')

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3), textcoords='offset points', ha='center', fontsize=10, color='black')

ax.set_title("Monthly Rainfall", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Rainfall (mm)", fontsize=14)

month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticks(months)
ax.set_xticklabels(month_labels, fontsize=12)

plt.tight_layout()
plt.show()