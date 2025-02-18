import matplotlib.pyplot as plt
import numpy as np

# Define years and revenue data
years = np.arange(2013, 2023)
revenue = np.array([0.5, 2.1, 3.9, 7.0, 10.2, 13.5, 18.0, 24.0, 32.5, 45.0])

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the revenue data
ax.plot(years, revenue, marker='o', linestyle='-', color='darkred', lw=2, markersize=8)

# Add titles and labels
ax.set_title('Annual Revenue Progression of InnovateTech (2013-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Revenue (in millions USD)', fontsize=14)

# Annotate each data point with revenue values
for i in range(len(years)):
    ax.text(years[i], revenue[i] + 1, f'{revenue[i]:.1f}', ha='center', fontsize=10, color='darkred')

# Remove unnecessary aspects
ax.tick_params(axis='both', which='major', labelsize=12)
plt.xticks(np.arange(2013, 2023, step=1))
plt.tight_layout()

# Display the plot
plt.show()