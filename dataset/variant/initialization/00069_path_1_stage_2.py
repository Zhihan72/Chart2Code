import matplotlib.pyplot as plt
import numpy as np

# Define disciplines and funding sources
disciplines = ['Sciences', 'Engineering', 'Humanities', 'Social Sciences']
funding_sources = ['Government Grants', 'Private Sector', 'University Funds', 'Non-Profit Organizations']

# Data: Amount of funding in million USD
funding_data = np.array([
    [60, 30, 20, 10],  # Sciences
    [70, 20, 30, 15],  # Engineering
    [20, 10, 40, 30],  # Humanities
    [40, 15, 25, 20],  # Social Sciences
])

# Number of disciplines and sources
num_disciplines = len(disciplines)
num_sources = len(funding_sources)

# Set width of bar
bar_width = 0.2

# Set up colors for different funding sources
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create the grouped bar chart
fig, ax = plt.subplots(figsize=(10, 7))
index = np.arange(num_disciplines)

# Plot bars for each funding source
for i in range(num_sources):
    ax.bar(index + i*bar_width, funding_data[:, i], width=bar_width, color=colors[i], alpha=0.85)

# Customize the y-axis
ax.set_yticks(np.arange(0, 81, 10))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()