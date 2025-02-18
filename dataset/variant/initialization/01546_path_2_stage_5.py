import matplotlib.pyplot as plt
import numpy as np

# Existing data
sectors = ['FinTech', 'Artificial Intelligence', 'GreenTech', 'HealthTech', 'EdTech']
funding_amounts = [275, 350, 150, 220, 180]
colors = ['#7986CB', '#FFD54F', '#FF8A65', '#4DB6AC', '#BA68C8']

# New data - added series
additional_sectors = ['BioTech', 'SpaceTech']
additional_funding = [130, 200]
additional_colors = ['#82B1FF', '#FFAB91']

# Combine existing and new data
sectors.extend(additional_sectors)
funding_amounts.extend(additional_funding)
colors.extend(additional_colors)

fig, ax = plt.subplots(figsize=(12, 8))
bar_positions = np.arange(len(sectors))
bars = ax.barh(bar_positions, funding_amounts, color=colors, edgecolor='black', alpha=0.85)

ax.set_yticks(bar_positions)
ax.set_yticklabels(sectors, fontsize=12)
ax.set_xlabel('Investment (Millions)', fontsize=14)

for bar in bars:
    width = bar.get_width()
    ax.text(width - 20, bar.get_y() + bar.get_height() / 2, f'{width}M',
            va='center', ha='right', color='white', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()