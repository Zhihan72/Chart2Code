import matplotlib.pyplot as plt
import numpy as np

disciplines = ['Tech Studies', 'Life Sciences', 'Humanities']
funding_sources = ['Uni Funds', 'Grants', 'Non-Profits', 'Industry Support']

funding_data = np.array([
    [70, 20, 25, 15],  
    [60, 30, 20, 10],  
    [40, 15, 25, 20],  
])

colors = ['#d62728', '#2ca02c', '#ff7f0e', '#1f77b4']
hatch_patterns = ['/', '\\', '|', '-']
edge_colors = ['black', 'grey', 'darkblue', 'darkred']

fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.2  
x_positions = np.arange(len(disciplines))

for i, source in enumerate(funding_sources):
    ax.bar(x_positions + i * bar_width, funding_data[:, i], bar_width,
           label=source, color=colors[i], alpha=0.85,
           edgecolor=edge_colors[i], hatch=hatch_patterns[i])

ax.set_title("Financial Contributions per Field\nin Hypothetical Institute", fontsize=15, fontweight='heavy')
ax.set_xlabel('Fields of Study', fontsize=11, style='italic')
ax.set_ylabel('Total Funds (Million USD)', fontsize=11, style='italic')

ax.set_xticks(x_positions + bar_width * (len(funding_sources) - 1) / 2)
ax.set_xticklabels(disciplines, rotation=30)
ax.legend(title='Contribution Sources', loc='lower center', bbox_to_anchor=(0.5, 1.05), fontsize='medium', ncol=4, frameon=True)

ax.yaxis.grid(True, linestyle='dashdot', alpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()