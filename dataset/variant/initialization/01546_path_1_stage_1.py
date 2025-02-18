import matplotlib.pyplot as plt
import numpy as np

sectors = ['HealthTech', 'EdTech', 'Artificial Intelligence', 'GreenTech', 'FinTech']
funding_amounts = [220, 180, 350, 150, 275]
colors = ['#7986CB', '#FFD54F', '#FF8A65', '#BA68C8', '#4DB6AC']

fig, ax = plt.subplots(figsize=(12, 8))
bar_positions = np.arange(len(sectors))
bars = ax.bar(bar_positions, funding_amounts, color=colors, edgecolor='black', alpha=0.85, width=0.6)

ax.set_xticks(bar_positions)
ax.set_xticklabels(sectors, rotation=15, ha='right', fontsize=12)

# Randomly altered title and labels
ax.set_title('Funding Analysis of Various Sectors (2023)\nin the Technology Space', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Business Sectors', fontsize=14)
ax.set_ylabel('Invested Amount (Million USD)', fontsize=14)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height - 10, f'{height}M', ha='center', va='bottom', fontsize=12, color='white', fontweight='bold')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()