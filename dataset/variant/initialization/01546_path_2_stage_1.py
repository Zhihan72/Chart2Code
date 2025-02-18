import matplotlib.pyplot as plt
import numpy as np

# Data for tech startup funding
sectors = ['Artificial Intelligence', 'FinTech', 'HealthTech', 'EdTech', 'GreenTech']
funding_amounts = [350, 275, 220, 180, 150]
# Shuffled colors
colors = ['#FFD54F', '#BA68C8', '#7986CB', '#4DB6AC', '#FF8A65']

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bar_positions = np.arange(len(sectors))
bars = ax.bar(bar_positions, funding_amounts, color=colors, edgecolor='black', alpha=0.85, width=0.6)

ax.set_xticks(bar_positions)
ax.set_xticklabels(sectors, rotation=15, ha='right', fontsize=12)
ax.set_title('Venture Capital Funding Distribution\nin Silicon Valley Tech Sectors (2023)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Tech Sectors', fontsize=14)
ax.set_ylabel('Funding Amount (Million USD)', fontsize=14)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height - 10, f'{height}M', 
            ha='center', va='bottom', fontsize=12, color='white', fontweight='bold')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()