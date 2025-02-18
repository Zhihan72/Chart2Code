import matplotlib.pyplot as plt
import numpy as np

# Data for the 12 months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
index_A = np.array([1000, 1050, 1020, 1080, 1120, 1150, 1170, 1200, 1180, 1220, 1250, 1280])
index_B = np.array([980, 1020, 1010, 1040, 1070, 1100, 1130, 1150, 1180, 1200, 1230, 1270])
index_C = np.array([950, 1000, 1050, 1025, 1100, 1140, 1100, 1150, 1200, 1250, 1300, 1350])

# Create the plot
fig, ax = plt.subplots(figsize=(16, 9))

# Plot lines for each index
ax.plot(months, index_A, marker='o', linestyle='-', linewidth=2, color='#3498db')
ax.plot(months, index_B, marker='^', linestyle='-', linewidth=2, color='#e74c3c')
ax.plot(months, index_C, marker='s', linestyle='-', linewidth=2, color='#2ecc71')

# Add title and labels
ax.set_title('Performance Comparison of Market Indices in 2023', fontsize=20, fontweight='bold', pad=20)
ax.set_xlabel('Months', fontsize=16)
ax.set_ylabel('Index Value', fontsize=16)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()