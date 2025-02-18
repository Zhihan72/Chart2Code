import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

farm_a_productivity = np.array([42, 35, 52, 40, 45, 55, 58, 60, 50, 70, 65])
farm_b_productivity = np.array([38, 30, 53, 32, 42, 35, 50, 60, 45, 65, 55])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, farm_a_productivity, color='purple', linestyle='-.', linewidth=2, marker='s', label='Field X')
ax.plot(years, farm_b_productivity, color='orange', linestyle='-', linewidth=2, marker='^', label='Field Y')

highlight_year = 2015
highlight_a = farm_a_productivity[years.tolist().index(highlight_year)]
highlight_b = farm_b_productivity[years.tolist().index(highlight_year)]
ax.annotate(f"Unexpected Rise\nin {highlight_year}", xy=(highlight_year, highlight_a), xytext=(highlight_year, highlight_a + 10),
            arrowprops=dict(facecolor='gray', shrink=0.05, width=1.5),
            fontsize=12, ha='center', va='bottom', bbox=dict(boxstyle="round,pad=0.3", edgecolor='purple', facecolor='white'))

ax.annotate(f"Unusual Growth\nin {highlight_year}", xy=(highlight_year, highlight_b), xytext=(highlight_year + 1, highlight_b - 15),
            arrowprops=dict(facecolor='gray', shrink=0.05, width=1.5),
            fontsize=12, ha='center', va='top', bbox=dict(boxstyle="round,pad=0.3", edgecolor='orange', facecolor='white'))

ax.set_title("Fruit Production Growth Over a Decade (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Timeline", fontsize=12, fontweight='bold')
ax.set_ylabel("Output Volume (tons)", fontsize=12, fontweight='bold')

ax.grid(visible=False)
ax.legend(title='Fields', title_fontsize=12, fontsize=10, loc='lower right')

plt.tight_layout()
plt.show()