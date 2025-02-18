import matplotlib.pyplot as plt
import numpy as np

sectors = ['FinTech', 'GreenTech', 'Artificial Intelligence', 'HealthTech', 'EdTech']
funding_amounts = [275, 150, 350, 220, 180]
single_color = '#4DB6AC'

fig, ax = plt.subplots(figsize=(12, 8))
bar_positions = np.arange(len(sectors))
bars = ax.barh(bar_positions, funding_amounts, color=single_color, alpha=0.85)

ax.set_yticks(bar_positions)
ax.set_yticklabels(sectors, fontsize=12)

ax.set_title('Funding Analysis of Various Sectors (2023)\nin the Technology Space', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Invested Amount (Million USD)', fontsize=14)
ax.set_ylabel('Business Sectors', fontsize=14)

for bar in bars:
    width = bar.get_width()
    ax.text(width - 15, bar.get_y() + bar.get_height()/2, f'{width}M', ha='right', va='center', fontsize=12, color='white', fontweight='bold')

plt.tight_layout()
plt.show()