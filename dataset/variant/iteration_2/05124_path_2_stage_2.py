import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
# Manually shuffled or altered values within the original dataset structure
index_A = np.array([1150, 1000, 1080, 1020, 1120, 1050, 1200, 1170, 1250, 1180, 1220, 1280])
index_B = np.array([1020, 980, 1040, 1100, 1010, 1070, 1180, 1230, 1130, 1150, 1200, 1270])
index_C = np.array([1100, 950, 1250, 1300, 1000, 1050, 1140, 1025, 1100, 1150, 1200, 1350])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, index_A, marker='D', linestyle='--', linewidth=2.5, color='#FF5733', label='Index A')
ax.plot(months, index_B, marker='*', linestyle=':', linewidth=2.5, color='#33FFB5', label='Index B')
ax.plot(months, index_C, marker='x', linestyle='-.', linewidth=2.5, color='#3375FF', label='Index C')

ax.set_title('Market Index Trends for 2023', fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Index Value', fontsize=14)

ax.legend(title='Indices', title_fontsize=13, fontsize=11, loc='lower right', facecolor='lightgrey', edgecolor='black')

milestones = [
    ('Feb', 1000, 'Peak A in Feb'),
    ('Apr', 1250, 'C in Spring'),
    ('Jul', 1140, 'B rises midyear'),
    ('Dec', 1350, 'C tops in Dec')
]
for month, value, text in milestones:
    ax.annotate(text, xy=(month, value), xytext=(month, value + 70),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='black'),
                fontsize=9, bbox=dict(boxstyle="round,pad=0.2", edgecolor='black', facecolor='lightblue', alpha=0.4))

ax.grid(linestyle='-', alpha=0.4)
plt.tight_layout()
plt.show()