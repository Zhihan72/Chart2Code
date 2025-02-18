import matplotlib.pyplot as plt
import numpy as np

sectors = ['Artificial Intelligence', 'FinTech', 'HealthTech', 'EdTech', 'GreenTech']
funding_amounts = [350, 275, 220, 180, 150]
colors = ['#FFD54F', '#7986CB', '#4DB6AC', '#BA68C8', '#FF8A65']

fig, ax = plt.subplots(figsize=(12, 8))
bar_positions = np.arange(len(sectors))
bars = ax.barh(bar_positions, funding_amounts, color=colors, edgecolor='black', alpha=0.85)

ax.set_yticks(bar_positions)
ax.set_yticklabels(sectors, fontsize=12)
ax.set_xlabel('Funding Amount (Million USD)', fontsize=14)

for bar in bars:
    width = bar.get_width()
    ax.text(width - 30, bar.get_y() + bar.get_height() / 2, f'{width}M', 
            va='center', ha='right', color='white', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()