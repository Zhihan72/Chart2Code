import matplotlib.pyplot as plt
import numpy as np

# Define disciplines and funding sources with altered textual elements
disciplines = ['Tech Studies', 'Life Sciences', 'Humanities']
funding_sources = ['Uni Funds', 'Grants', 'Non-Profits', 'Industry Support']

# Data: Amount of funding in million USD
funding_data = np.array([
    [70, 20, 25, 15],  # Updated Tech Studies
    [60, 30, 20, 10],  # Life Sciences
    [40, 15, 25, 20],  # Humanities
])

# Set up colors for different funding sources
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(10, 7))
bottom = np.zeros(len(disciplines))

for i, source in enumerate(funding_sources):
    ax.bar(disciplines, funding_data[:, i], label=source, bottom=bottom, color=colors[i], alpha=0.85)
    bottom += funding_data[:, i]

# Altered plot details
ax.set_title("Financial Contributions per Field\nin Hypothetical Institute", fontsize=14, fontweight='bold')
ax.set_xlabel('Fields of Study', fontsize=12)
ax.set_ylabel('Total Funds (Million USD)', fontsize=12)
ax.legend(title='Contribution Sources', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')

# Customize the y-axis
ax.set_yticks(np.arange(0, 141, 20))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels if needed
plt.xticks(rotation=15)

# Automatically adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()