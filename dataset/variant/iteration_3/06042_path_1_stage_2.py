import matplotlib.pyplot as plt
import numpy as np

# Data
sleep_hours = np.array([5, 6, 7, 8, 9, 10])
productivity_scores = np.array([60, 65, 70, 80, 85, 90])

# Create horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(sleep_hours, productivity_scores, color='skyblue', edgecolor='gray')

# Customize axes and labels
plt.title('Sleep vs. Productivity', fontsize=14, style='italic', color='darkblue')
plt.xlabel('Productivity Score', fontsize=11, color='darkgreen')
plt.ylabel('Sleep Duration (hours)', fontsize=11, color='darkred')
plt.grid(visible=True, linestyle='-', alpha=0.3)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()