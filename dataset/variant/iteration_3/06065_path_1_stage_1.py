import matplotlib.pyplot as plt
import numpy as np

# Technology sectors and their initial funding amounts (in million USD)
sectors = ["AI", "Blockchain", "Internet of Things", "Cyber Security", "Quantum Computing"]
initial_funding = [10, 8, 7, 6, 5]

# Year-end revenue for each sector (in million USD)
year_end_revenue = [15, 12, 11, 10, 7]

# Calculate percentage growth
growth_percentage = [(rev - init) / init * 100 for init, rev in zip(initial_funding, year_end_revenue)]

# Creating the bar chart to show the final results of the challenge
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the initial funding
bars_initial = ax.bar(np.arange(len(sectors)) - 0.2, initial_funding, width=0.4, color='#1f77b4')

# Plot the year-end revenue
bars_revenue = ax.bar(np.arange(len(sectors)) + 0.2, year_end_revenue, width=0.4, color='#ff7f0e')

# Title and axis labels
ax.set_title('TechVille Tech Innovation Challenge Results', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Technology Sectors', fontsize=12)
ax.set_ylabel('Amount (Million USD)', fontsize=12)
ax.set_xticks(np.arange(len(sectors)))
ax.set_xticklabels(sectors)

# Labeling each bar with the respective values
ax.bar_label(bars_initial, padding=3, fontsize=10)
ax.bar_label(bars_revenue, padding=3, fontsize=10)

# Adding a line plot for growth percentage
ax2 = ax.twinx()
ax2.plot(np.arange(len(sectors)), growth_percentage, color='green', marker='o', linestyle='--', linewidth=2)
ax2.set_ylabel('Growth Percentage (%)', fontsize=12)
ax2.set_ylim(0, max(growth_percentage) + 10)

# Annotate the growth percentage values
for i, gp in enumerate(growth_percentage):
    ax2.text(i, gp + 1, f'{gp:.1f}%', ha='center', va='bottom', color='green', fontsize=10, fontweight='bold')

# Remove grid and spines (borders)
ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Layout adjustments
plt.tight_layout()
plt.show()