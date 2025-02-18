import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Drama clubs in various fictional high schools are hosting annual performances. 
# We want to compare production budgets across different schools over five years. 
# The goal is to see how investment in dramas has changed and which schools are spending the most.

# Fictional high schools
schools = ['Hogwarts High', 'Rivendell Academy', 'Narnia Unified', 'Westeros Prep', 'Middle-Earth School']

# Budget data over five years (in thousand dollars)
budgets_2018 = np.array([35, 40, 25, 30, 45])
budgets_2019 = np.array([40, 38, 30, 33, 50])
budgets_2020 = np.array([50, 45, 35, 38, 55])
budgets_2021 = np.array([55, 50, 40, 42, 60])
budgets_2022 = np.array([65, 55, 45, 50, 70])

years = ['2018', '2019', '2020', '2021', '2022']
data = np.array([budgets_2018, budgets_2019, budgets_2020, budgets_2021, budgets_2022])

# Set up the bar plot
fig, ax = plt.subplots(figsize=(12, 8))

# Define the bar width and positions
bar_width = 0.15
bar_positions = np.arange(len(schools))

# Colors for each year
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot bars for each year
for idx, year in enumerate(years):
    ax.bar(bar_positions + idx * bar_width, data[idx], bar_width, label=f'{year}', color=colors[idx])

# Customize the plot
ax.set_xlabel('High Schools', fontsize=14)
ax.set_ylabel('Production Budget (in thousand USD)', fontsize=14)
ax.set_title('Annual Production Budgets for Drama Performances (2018-2022)\nAcross Fictional High Schools', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(bar_positions + bar_width * 2)
ax.set_xticklabels(schools, rotation=45, ha="right", fontsize=12)
ax.legend(title='Year', fontsize=12)

# Add grid and enhance visual aesthetics
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
fig.tight_layout()

# Show the plot
plt.show()