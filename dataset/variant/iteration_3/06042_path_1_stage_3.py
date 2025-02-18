import matplotlib.pyplot as plt
import numpy as np

# Data
sleep_hours = np.array([5, 6, 7, 8, 9, 10])
productivity_scores = np.array([60, 65, 70, 80, 85, 90])
leisure_hours = np.array([2, 3, 4, 5, 6, 7])  # Added additional data series
leisure_productivity_scores = np.array([55, 60, 68, 75, 80, 85])  # Corresponding productivity scores

# Create horizontal bar chart
plt.figure(figsize=(12, 7))
plt.barh(sleep_hours, productivity_scores, color='skyblue', edgecolor='gray', label='Sleep')
plt.barh(leisure_hours, leisure_productivity_scores, color='lightcoral', edgecolor='gray', alpha=0.7, label='Leisure')

# Customize axes and labels
plt.title('Impact of Sleep and Leisure on Productivity', fontsize=14, style='italic', color='darkblue')
plt.xlabel('Productivity Score', fontsize=11, color='darkgreen')
plt.ylabel('Hours', fontsize=11, color='darkred')
plt.grid(visible=True, linestyle='-', alpha=0.3)

# Add legend
plt.legend(loc='lower right')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()