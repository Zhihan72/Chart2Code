import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The data represents the performance of three different market indices (represented by Index A, Index B, and Index C) 
# over a span of 12 months in a year. This comparison is aimed at financial analysts and investors 
# who want to understand the trends and disparities among the indices.

# Data for the 12 months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
index_A = np.array([1000, 1050, 1020, 1080, 1120, 1150, 1170, 1200, 1180, 1220, 1250, 1280])
index_B = np.array([980, 1020, 1010, 1040, 1070, 1100, 1130, 1150, 1180, 1200, 1230, 1270])
index_C = np.array([950, 1000, 1050, 1025, 1100, 1140, 1100, 1150, 1200, 1250, 1300, 1350])

# Create the plot
fig, ax = plt.subplots(figsize=(16, 9))

# Plot lines for each index
ax.plot(months, index_A, marker='o', linestyle='-', linewidth=2, color='#3498db', label='Index A')
ax.plot(months, index_B, marker='^', linestyle='-', linewidth=2, color='#e74c3c', label='Index B')
ax.plot(months, index_C, marker='s', linestyle='-', linewidth=2, color='#2ecc71', label='Index C')

# Add title and labels
ax.set_title('Performance Comparison of Market Indices in 2023', fontsize=20, fontweight='bold', pad=20)
ax.set_xlabel('Months', fontsize=16)
ax.set_ylabel('Index Value', fontsize=16)

# Add legend
ax.legend(title='Market Indices', title_fontsize=14, fontsize=12, loc='upper left')

# Highlight key milestones with annotations
milestones = [
    ('Apr', 1080, 'Index A peaks in April'),
    ('May', 1100, 'Index B gains momentum in May'),
    ('Aug', 1150, 'Index C growth in summer'),
    ('Dec', 1350, 'Index C surpasses all by year end')
]
for month, value, text in milestones:
    ax.annotate(text, xy=(month, value), xytext=(month, value + 80),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='gray'),
                fontsize=10, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.5))

# Add grid
ax.grid(linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()