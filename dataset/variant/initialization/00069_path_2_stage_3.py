import matplotlib.pyplot as plt
import numpy as np

disciplines = ['Tech Studies', 'Life Sciences', 'Humanities']
funding_sources = ['Uni Funds', 'Grants', 'Non-Profits', 'Industry Support']

funding_data = np.array([
    [70, 20, 25, 15],  
    [60, 30, 20, 10],  
    [40, 15, 25, 20],  
])

# Shuffled colors to alter style.
colors = ['#d62728', '#2ca02c', '#ff7f0e', '#1f77b4']

fig, ax = plt.subplots(figsize=(10, 7))
bottom = np.zeros(len(disciplines))

# Altered marker styles (edge color, hatch patterns).
hatch_patterns = ['/', '\\', '|', '-']
edge_colors = ['black', 'grey', 'darkblue', 'darkred']

for i, source in enumerate(funding_sources):
    ax.bar(disciplines, funding_data[:, i], label=source, bottom=bottom,
           color=colors[i], alpha=0.85, edgecolor=edge_colors[i], hatch=hatch_patterns[i])
    bottom += funding_data[:, i]

# Changed font size and added new styles dynamically.
ax.set_title("Financial Contributions per Field\nin Hypothetical Institute", fontsize=15, fontweight='heavy')
ax.set_xlabel('Fields of Study', fontsize=11, style='italic')
ax.set_ylabel('Total Funds (Million USD)', fontsize=11, style='italic')

# Legend modified to appear on top with a border
ax.legend(title='Contribution Sources', loc='lower center', bbox_to_anchor=(0.5, 1.05), fontsize='medium', ncol=4, frameon=True)

# Altered y-axis line style and enhanced grid
ax.yaxis.grid(True, linestyle='dashdot', alpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()