import matplotlib.pyplot as plt
import numpy as np

# Backstory and Title:
# Our chart will visualize the internet usage growth among different age groups over a span of 20 years (2000-2020). This is to understand how different age demographics have embraced the internet over time.

# Define data
years = np.arange(2000, 2021)
age_groups = ["Teens", "20s", "30s", "40s", "50s+", "Seniors"]

# Internet usage percentages for each age group over time
teens = [5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 75, 80, 85, 88, 90, 92, 94, 95, 96, 97]
twenties = [10, 15, 25, 35, 50, 55, 60, 65, 70, 75, 80, 82, 83, 85, 86, 87, 88, 89, 90, 90, 90]
thirties = [5, 8, 12, 18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 68, 70, 72, 74, 76, 78, 80, 82]
forties = [3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 62, 63, 64, 65, 66, 67, 68, 70]
fifties_plus = [1, 2, 5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 48, 50, 52, 54, 56, 58, 60]
seniors = [0, 1, 2, 3, 4, 5, 6, 8, 10, 13, 15, 17, 19, 21, 23, 24, 25, 26, 27, 28, 30]

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors and markers for the lines
colors = ['#FF0000', '#00A2FF', '#56B4E9', '#F0E442', '#009E73', '#E69F00']
markers = ['o', 's', 'D', '^', 'v', 'x']

# Plot the data
for data, name, color, marker in zip([teens, twenties, thirties, forties, fifties_plus, seniors], age_groups, colors, markers):
    ax.plot(years, data, label=name, color=color, marker=marker, linewidth=2, linestyle='-')
    # Annotate end points
    ax.annotate(f'{data[-1]}%', xy=(years[-1], data[-1]), xytext=(5, -5), textcoords='offset points', ha='center', fontsize=9, color=color)

# Title and axis labels
ax.set_title('Evolution of Internet Usage Among Different Age Groups\n(2000-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Internet Usage Percentage (%)', fontsize=12)

# Add legend
ax.legend(title='Age Groups', title_fontsize='13', loc='upper left', frameon=False)

# Add gridlines
ax.grid(True, linestyle='--', which='major', color='grey', alpha=0.3)

# Set limits for better visualization
ax.set_xlim(2000, 2020)
ax.set_ylim(0, 100)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()