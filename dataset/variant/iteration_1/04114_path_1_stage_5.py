import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
rainfall = np.array([85, 78, 92, 110, 134, 158, 102, 75, 65, 45, 40, 70])
avg_temperature = np.array([3, 5, 9, 12, 16, 20, 23, 22, 18, 14, 8, 5])

sorted_indices = np.argsort(rainfall)
sorted_rainfall = rainfall[sorted_indices]
sorted_avg_temp = avg_temperature[sorted_indices]
sorted_month_labels = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])[sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.bar(sorted_month_labels, sorted_rainfall, color='lightcoral', edgecolor='darkred', hatch='/')
for bar in ax1.containers[0]:
    height = bar.get_height()
    ax1.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                 xytext=(-10, 3), textcoords='offset points', rotation=45, ha='center', fontsize=12, color='navy')

ax1.set_title("Monthly Rainfall and Temperature", fontsize=18, fontweight='heavy', pad=20, color='darkgreen')
ax1.set_xlabel("Month", fontsize=14, style='italic', color='teal')
ax1.set_ylabel("Rainfall (mm)", fontsize=14, style='italic', color='teal')
ax1.grid(axis='y', color='gray', linestyle='-.', linewidth=1, alpha=0.8)
ax1.spines['top'].set_linewidth(2)
ax1.spines['right'].set_linewidth(2)
ax1.spines['bottom'].set_linewidth(1.5)
ax1.spines['left'].set_linewidth(1.5)

ax2 = ax1.twinx()
ax2.plot(sorted_month_labels, sorted_avg_temp, color='blue', marker='o', linestyle='-', linewidth=2)
ax2.set_ylabel("Average Temperature (°C)", fontsize=14, style='italic', color='blue')

plt.tight_layout()
plt.show()