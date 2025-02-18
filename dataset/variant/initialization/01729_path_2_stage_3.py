import matplotlib.pyplot as plt
import numpy as np

countries = ['USA', 'China', 'Germany', 'India', 'Brazil']
total_investments = np.array([50, 70, 35, 65, 40])  # Randomly altered
colors = ['#20B2AA', '#FFA07A', '#dda0dd', '#4682B4', '#98fb98']  # Adjusted colors

fig, ax = plt.subplots(figsize=(12, 7))

ax.bar(countries, total_investments, color=colors, edgecolor='black', width=0.6)

ax.set_title('2023 RE Investments', fontsize=16, fontweight='bold')
ax.set_ylabel('Investments (B USD)', fontsize=12)
ax.set_xlabel('Countries', fontsize=12)

for i, investment in enumerate(total_investments):
    ax.text(i, investment + 1, f"${investment}B", color='black', ha='center', va='bottom', fontsize=10)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()