import matplotlib.pyplot as plt
import numpy as np

countries = ['Country X', 'Nation Y', 'Region Z', 'Empire V']
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])

co2_reductions = np.array([
    [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0],
    [0.3, 0.32, 0.34, 0.37, 0.4, 0.42, 0.45, 0.48, 0.5, 0.52, 0.55],
    [0.2, 0.23, 0.25, 0.28, 0.3, 0.33, 0.35, 0.38, 0.4, 0.43, 0.45],
    [0.1, 0.13, 0.15, 0.17, 0.2, 0.22, 0.25, 0.27, 0.3, 0.33, 0.35]
])

plt.figure(figsize=(14, 8))

marker_styles = ['s', '^', 'x', 'd']
line_styles = ['-', '--', '-.', '-']
for i, country in enumerate(countries):
    plt.plot(years, co2_reductions[i], marker=marker_styles[i], linestyle=line_styles[i], label=country)

milestones = {
    2013: ("Accord Beta", 0.72),
    2016: ("Treaty Gamma", 0.77),
    2019: ("Charter Delta", 0.88)
}

for year, (text, level) in milestones.items():
    plt.annotate(text,
                 xy=(year, level),
                 xytext=(year, level + 0.12),
                 arrowprops=dict(facecolor='darkred', shrink=0.05, width=1, headwidth=8),
                 fontsize=10, color='purple')

for (x, country_data) in zip(years, co2_reductions):
    for (country, y) in zip(countries, country_data):
        plt.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=8)

plt.title('Worldwide CO2 U-Turns (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Calendar Year', fontsize=14)
plt.ylabel('CO2 Reduction (Billion Tons)', fontsize=14)
plt.xticks(years)

plt.grid(axis='x', linestyle='-.', color='gray', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.legend(title='Regions', loc='lower right', fontsize=9, title_fontsize='11')

plt.tight_layout()
plt.show()