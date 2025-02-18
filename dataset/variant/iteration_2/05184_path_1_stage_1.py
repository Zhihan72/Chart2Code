import numpy as np
import matplotlib.pyplot as plt

# Sectors and total revenue data aggregated and sorted
sectors = ['Cybersecurity', 'IoT', 'AI', 'Cloud Computing']
total_revenues = np.array([45, 63, 90, 118])
colors = ['#FFD700', '#4682B4', '#FF6347', '#32CD32']

# Setup the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the sorted bar chart
ax.bar(sectors, total_revenues, color=colors)

# Labeling and titling the plot
ax.set_xlabel('Sectors', fontsize=14)
ax.set_ylabel('Total Revenue (in Billion USD)', fontsize=14)
ax.set_title('Total Revenue by Sector from 2019 to 2022', fontsize=16, fontweight='bold')

# Display the plot
plt.tight_layout()
plt.show()