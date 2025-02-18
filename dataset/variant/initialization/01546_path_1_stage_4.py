import matplotlib.pyplot as plt
import numpy as np

sectors = ['FinTech', 'GreenTech', 'Artificial Intelligence', 'HealthTech', 'EdTech']
funding_amounts = [275, 150, 350, 220, 180]
single_color = '#4DB6AC'  # Use a consistent color for all bars

fig, ax = plt.subplots(figsize=(12, 8))
bar_positions = np.arange(len(sectors))
bars = ax.bar(bar_positions, funding_amounts, color=single_color, alpha=0.85, width=0.6)

ax.set_xticks(bar_positions)
ax.set_xticklabels(sectors, rotation=15, ha='right', fontsize=12)

ax.set_title('Funding Analysis of Various Sectors (2023)\nin the Technology Space', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Business Sectors', fontsize=14)
ax.set_ylabel('Invested Amount (Million USD)', fontsize=14)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height - 10, f'{height}M', ha='center', va='bottom', fontsize=12, color='white', fontweight='bold')

plt.tight_layout()
plt.show()