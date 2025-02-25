import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
index_A = np.array([1000, 1050, 1020, 1080, 1120, 1150, 1170, 1200, 1180, 1220, 1250, 1280])
index_B = np.array([980, 1020, 1010, 1040, 1070, 1100, 1130, 1150, 1180, 1200, 1230, 1270])
index_C = np.array([950, 1000, 1050, 1025, 1100, 1140, 1100, 1150, 1200, 1250, 1300, 1350])

fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each index with altered stylistic elements
ax.plot(months, index_A, marker='D', linestyle='--', linewidth=2.5, color='#FF5733', label='Index A')
ax.plot(months, index_B, marker='*', linestyle=':', linewidth=2.5, color='#33FFB5', label='Index B')
ax.plot(months, index_C, marker='x', linestyle='-.', linewidth=2.5, color='#3375FF', label='Index C')

# Modify title and labels
ax.set_title('Market Index Trends for 2023', fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Index Value', fontsize=14)

# Change legend location and styles
ax.legend(title='Indices', title_fontsize=13, fontsize=11, loc='lower right', facecolor='lightgrey', edgecolor='black')

# Annotate with potentially key highlights, changing the appearance
milestones = [
    ('Apr', 1080, 'Peak A in Apr'),
    ('May', 1100, 'B rises in May'),
    ('Aug', 1150, 'C in Summer'),
    ('Dec', 1350, 'C tops in Dec')
]
for month, value, text in milestones:
    ax.annotate(text, xy=(month, value), xytext=(month, value + 70),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='black'),
                fontsize=9, bbox=dict(boxstyle="round,pad=0.2", edgecolor='black', facecolor='lightblue', alpha=0.4))

# Modify grid
ax.grid(linestyle='-', alpha=0.4)

# Adjust layout
plt.tight_layout()

plt.show()