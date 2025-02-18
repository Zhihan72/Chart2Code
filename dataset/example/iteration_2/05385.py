import matplotlib.pyplot as plt
import numpy as np

# Title and backstory
# The plot is about the fictional growth trends of three different types of AI models over a span of 10 years in terms of technology advancement metrics.
# Based on this fictional scenario, we'll create data for three AI models: Alpha, Beta, and Gamma.

# Define the years
years = np.arange(2013, 2023)

# Technology advancement metrics for each AI model
alpha_advancement = np.array([20, 25, 32, 40, 50, 62, 75, 90, 108, 125])
beta_advancement = np.array([15, 22, 31, 42, 58, 72, 85, 104, 120, 140])
gamma_advancement = np.array([10, 18, 25, 34, 47, 55, 68, 84, 100, 115])

# Calculate cumulative advancements
alpha_cumulative = np.cumsum(alpha_advancement)
beta_cumulative = np.cumsum(beta_advancement)
gamma_cumulative = np.cumsum(gamma_advancement)

# Plot setup with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), sharex=True)

# Line plot of annual advancements on the first subplot
ax1.plot(years, alpha_advancement, label='Alpha Model', color='b', marker='o', linestyle='--', linewidth=2)
ax1.plot(years, beta_advancement, label='Beta Model', color='g', marker='s', linestyle='-.', linewidth=2)
ax1.plot(years, gamma_advancement, label='Gamma Model', color='r', marker='^', linestyle='-', linewidth=2)

# Add title, labels, and grid for the first subplot
ax1.set_title('Annual Technological Advancements\nof AI Models (2013-2022)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Advancement Metric', fontsize=12)
ax1.legend(title='AI Models', loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Annotate significant advancement points
ax1.annotate('Significant Growth', xy=(2018, 62), xytext=(2016, 80),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')
ax1.annotate('Peak Jump', xy=(2021, 120), xytext=(2019, 140),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')

# Second subplot: Bar chart for cumulative advancements
width = 0.25
ax2.bar(years - width, alpha_cumulative, width=width, color='b', alpha=0.6, label='Alpha Model')
ax2.bar(years, beta_cumulative, width=width, color='g', alpha=0.6, label='Beta Model')
ax2.bar(years + width, gamma_cumulative, width=width, color='r', alpha=0.6, label='Gamma Model')

# Add title, labels, and grid for the second subplot
ax2.set_title('Cumulative Technological Advancements\nof AI Models', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Cumulative Advancement Metric', fontsize=12)
ax2.legend(title='AI Models', loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()