import matplotlib.pyplot as plt
import numpy as np

years = np.array(range(1980, 2020, 5))
country_a_production = np.array([4, 14, 28, 49, 80, 120, 185, 243])
country_b_production = np.array([2, 12, 25, 60, 90, 140, 210, 275])
country_c_production = np.array([1, 5, 15, 35, 60, 105, 180, 240])
country_d_production = np.array([3, 10, 20, 45, 70, 100, 165, 220]) # Data for new Country D

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, country_a_production, marker='o', linestyle='-', linewidth=2, color='crimson')
ax.plot(years, country_b_production, marker='s', linestyle='-', linewidth=2, color='teal')
ax.plot(years, country_c_production, marker='^', linestyle='-', linewidth=2, color='goldenrod')
ax.plot(years, country_d_production, marker='x', linestyle='-', linewidth=2, color='purple') # Plotting Country D

for i, (a, b, c, d) in enumerate(zip(country_a_production, country_b_production, country_c_production, country_d_production)):
    ax.text(years[i], a + 5, f'{a}TWh', ha='center', fontsize=9, color='darkred', fontweight='bold')
    ax.text(years[i], b - 12, f'{b}TWh', ha='center', fontsize=9, color='darkcyan', fontweight='bold')
    ax.text(years[i], c + 5, f'{c}TWh', ha='center', fontsize=9, color='darkgoldenrod', fontweight='bold')
    ax.text(years[i], d + 5, f'{d}TWh', ha='center', fontsize=9, color='indigo', fontweight='bold') # Annotating Country D

plt.title("Renewable Energy Production Over Time\nFor Four Countries (1980-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Renewable Energy Production (Terawatt-hours)", fontsize=14)

plt.tight_layout()
plt.show()