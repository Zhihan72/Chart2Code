import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2026)
ai_innovation = np.array([20, 22, 24, 26, 30, 34, 40, 48, 60, 75, 95, 120, 150, 185, 230, 280, 350, 430, 525, 630, 750, 880, 1020, 1175, 1350, 1550])
renewable_energy = np.array([10, 12, 15, 18, 22, 28, 35, 44, 56, 70, 86, 105, 127, 153, 183, 218, 260, 308, 364, 428, 502, 586, 682, 790, 912, 1050])
space_exploration = np.array([3, 4, 5, 6, 8, 11, 15, 21, 28, 37, 48, 62, 79, 100, 125, 155, 190, 230, 276, 328, 388, 455, 530, 615, 710, 815])

fig, ax = plt.subplots(figsize=(14, 8))

ax.fill_between(years, ai_innovation, label='Artificial Creativity', color='#ff6699', alpha=0.8, linestyle=':', hatch='/')
ax.fill_between(years, ai_innovation + renewable_energy, ai_innovation, label='Green Power', color='#66cc33', alpha=0.8, linestyle='--', hatch='\\')
ax.fill_between(years, ai_innovation + renewable_energy + space_exploration, ai_innovation + renewable_energy, label='Space Venture', color='#ffcc33', alpha=0.8, linestyle='-', hatch='o')

ax.set_title("Techno-Era: Innovation Surge across Eras", fontsize=18, weight='bold', pad=30)
ax.set_xlabel("Years", fontsize=14)
ax.set_ylabel("Impact Scale", fontsize=14)
ax.set_xticks(years[::2])
ax.tick_params(axis='x', rotation=45)
ax.grid(True, linestyle='-', linewidth=0.7, alpha=0.4)

ax.legend(loc='best', fontsize=12, title="Innovation Fields", title_fontsize='13', shadow=True)

highlight_years = [2010, 2020]
for year in highlight_years:
    ax.axvline(x=year, color='purple', linestyle=':', linewidth=1.5, alpha=0.6)
    ax.text(year, 1400, 'Key Milestone', rotation=90, verticalalignment='bottom', horizontalalignment='right')

plt.tight_layout()

plt.show()