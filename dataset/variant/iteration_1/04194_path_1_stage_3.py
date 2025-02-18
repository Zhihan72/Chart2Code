import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Artificially altered data for renewable energy production (MegaWatts) for three countries
country_data = {
    'EcoLand': [50, 58, 63, 69, 78, 90, 115, 120, 142, 165, 195, 230, 270, 315, 365, 420, 495, 555, 645, 740, 860],
    'GreenVille': [42, 44, 53, 59, 60, 75, 98, 108, 128, 152, 182, 225, 255, 310, 360, 412, 470, 550, 615, 710, 790],
    'Sustainia': [32, 37, 39, 48, 52, 68, 90, 102, 118, 143, 170, 215, 240, 290, 340, 395, 470, 530, 615, 685, 800]
}

global_growth_rate = np.array([41, 45, 47, 52, 54, 62, 68, 70, 80, 88, 97, 106, 117, 124, 136, 153, 162, 178, 197, 210, 232])

fig, ax1 = plt.subplots(figsize=(14, 8))
colors = ['#ffcccc', '#3399ff', '#66cc66']
markers = ['o', 'v', '^']

for (country, color, marker) in zip(country_data.keys(), colors, markers):
    ax1.plot(years, country_data[country], color=color, linewidth=2.5, marker=marker, markersize=5)

ax2 = ax1.twinx()
ax2.plot(years, global_growth_rate, color='grey', linestyle=(0, (5, 10)), linewidth=2.5)

ax1.set_xticks(np.arange(2000, 2021, 2))
ax1.grid(True, linestyle='-', which='major', axis='both', alpha=0.5)

for spine in ax1.spines.values():
    spine.set_edgecolor('#999999')
    spine.set_linewidth(1.5)

plt.tight_layout()
plt.show()