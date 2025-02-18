import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Manually shuffled data for each woodland
woodland_A = np.array([175, 152, 165, 159, 150, 170, 157, 178, 180, 185, 190])
woodland_B = np.array([137, 132, 158, 130, 145, 135, 142, 152, 160, 132, 162])
woodland_C = np.array([120, 115, 110, 112, 128, 126, 124, 117, 118, 130, 133])
woodland_D = np.array([106, 100, 95, 110, 102, 97, 112, 115, 108, 104, 117])

single_color = '#4682B4'
markers = ['^', 'd', 'o', 's']

fig, ax1 = plt.subplots(figsize=(14, 8))

woodlands_data = [woodland_A, woodland_B, woodland_C, woodland_D]
woodland_names = ["Park Alpha", "Grove Beta", "Forest Gamma", "Thicket Delta"]

for data, name, marker in zip(woodlands_data, woodland_names, markers):
    ax1.plot(years, data, label=name, color=single_color, marker=marker, linestyle='-.', linewidth=2, alpha=0.8)
    for (x, y) in zip(years, data):
        ax1.annotate(f'{y}', xy=(x, y), xytext=(0, 5),
                     textcoords='offset points', ha='center', fontsize=9, color=single_color)

ax1.set_title('Analysis of Biodiversity Initiatives:\nTracking Animal Populations in UK Greenlands (2010-2020)', 
              fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Observation Year', fontsize=14)
ax1.set_ylabel('Animal Count', fontsize=14)
ax1.grid(True, linestyle=':', alpha=0.4)

ax1.legend(title='Regions', title_fontsize='13', loc='best', frameon=True, shadow=True)

plt.xticks(years, rotation=45)
plt.ylim(90, 200)

plt.tight_layout()

plt.show()