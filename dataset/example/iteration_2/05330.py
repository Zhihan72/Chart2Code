import matplotlib.pyplot as plt
import numpy as np

# Context: Solar Panels Installed Per City Over Five Years
cities = ['Solton', 'Sunville', 'Raymont', 'Sunnyridge', 'Heliocity']
years = [2018, 2019, 2020, 2021, 2022]

# Data: Solar panels installed (in hundreds)
solar_installs = np.array([
    [20, 35, 40, 50, 65],  # Solton
    [25, 30, 45, 55, 70],  # Sunville
    [15, 25, 35, 45, 50],  # Raymont
    [10, 20, 30, 35, 40],  # Sunnyridge
    [12, 24, 36, 48, 60]   # Heliocity
])

# Set the positions of the bars
bar_width = 0.15
x = np.arange(len(years))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Colors for each city
colors = ['#FFA07A', '#20B2AA', '#FFB6C1', '#778899', '#F0E68C']

# Create a bar for each city
for i, city in enumerate(cities):
    ax.bar(x + i * bar_width, solar_installs[i], width=bar_width, label=city, color=colors[i])

# Customize the plot
ax.set_title('Solar Energy Adoption:\nNumber of Solar Panels Installed (2018-2022)', fontsize=16, fontweight='bold', pad=20, wrap=True)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Solar Panels Installed (Hundreds)', fontsize=13)
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(years)
ax.legend(title='Cities', fontsize=10, title_fontsize='11')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add text annotations on each bar for better insight
for i in range(len(cities)):
    for j in range(len(years)):
        ax.text(x[j] + i * bar_width, solar_installs[i, j] + 0.5, str(solar_installs[i, j]), ha='center', va='bottom', fontsize=9)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()