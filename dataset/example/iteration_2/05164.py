import matplotlib.pyplot as plt
import numpy as np

# Backstory: Annual Research Development Expenditure by Sector
# An imaginary tech summit reviews the consistent investment in R&D across various sectors over the past decade.

# Define sectors
sectors = ['Biotech', 'Cybersecurity', 'AI', 'Renewable Energy', 'Space Tech']

# Expenditure data for R&D in each sector (in millions of USD)
expenditure_data = [
    [100, 120, 130, 125, 140, 150, 135, 145, 155, 160],  # Biotech
    [75, 85, 80, 90, 110, 120, 115, 105, 100, 95],       # Cybersecurity
    [200, 220, 210, 230, 240, 250, 245, 255, 260, 275],  # AI
    [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],            # Renewable Energy
    [180, 190, 200, 195, 185, 210, 220, 225, 230, 235]   # Space Tech
]

# Scatter plot data indicating annual R&D growth rates per sector
years = np.arange(2013, 2023)

# Set up the plot with two subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Boxplot on the left
ax1 = axes[0]
bp = ax1.boxplot(expenditure_data, vert=False, patch_artist=True, showmeans=True, notch=True,
                 boxprops=dict(facecolor="#ffcccb", color="#8b0000", linewidth=1.2),
                 medianprops=dict(color="#0000cd", linewidth=1.5),
                 meanprops=dict(marker='D', markeredgecolor='black', markerfacecolor='lime'),
                 whiskerprops=dict(color="#8b0000"), capprops=dict(color="#8b0000"))

ax1.set_yticklabels(sectors, fontsize=11)
ax1.set_title("Decadal R&D Expenditure Distribution\nAcross Sectors (2013-2022)", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel("Expenditure (in millions USD)", fontsize=12)
ax1.set_ylabel("Sectors", fontsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# Scatter plot on the right
ax2 = axes[1]
growth_rates = [
    [10, 5, 20, 15, 10, 15, 5, 10, 15, 20],  # Biotech
    [8, 12, 5, 10, 20, 15, 10, 5, 8, 12],    # Cybersecurity
    [15, 10, 20, 15, 20, 10, 15, 20, 10, 15],# AI
    [5, 8, 12, 15, 5, 8, 10, 12, 15, 10],    # Renewable Energy
    [12, 10, 5, 20, 15, 10, 20, 15, 10, 12]  # Space Tech
]
for idx, sector_growth in enumerate(growth_rates):
    ax2.scatter(years, sector_growth, label=sectors[idx], s=100, alpha=0.7, edgecolors='w')

ax2.set_title("Annual R&D Growth Rates by Sector (2013-2022)", fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Growth Rate (%)", fontsize=12)
ax2.legend(title='Sectors', fontsize=9, title_fontsize=10)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.set_xticks(years)
ax2.set_xticklabels([str(yr) for yr in years], rotation=45, ha='right')

# Adjust layout for better fit
plt.tight_layout()

# Display the plots
plt.show()