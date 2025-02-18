import matplotlib.pyplot as plt
import numpy as np

years = np.array(range(1980, 2020, 5))
country_a_production = np.array([4, 14, 28, 49, 80, 120, 185, 243])
country_b_production = np.array([2, 12, 25, 60, 90, 140, 210, 275])
country_c_production = np.array([1, 5, 15, 35, 60, 105, 180, 240])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, country_a_production, marker='d', linestyle='--', linewidth=1.5, color='purple', label='Country A')
ax.plot(years, country_b_production, marker='x', linestyle='-', linewidth=1.5, color='teal', label='Country B')
ax.plot(years, country_c_production, marker='h', linestyle=':', linewidth=1.5, color='maroon', label='Country C')

for i, (a, b, c) in enumerate(zip(country_a_production, country_b_production, country_c_production)):
    ax.text(years[i], a + 5, f'{a}TWh', ha='center', fontsize=9, color='purple', fontweight='bold')
    ax.text(years[i], b - 12, f'{b}TWh', ha='center', fontsize=9, color='teal', fontweight='bold')
    ax.text(years[i], c + 5, f'{c}TWh', ha='center', fontsize=9, color='maroon', fontweight='bold')

plt.title("Renewable Energy Production Over Time\nFor Three Countries (1980-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Renewable Energy Production (Terawatt-hours)", fontsize=14)

ax.legend(title='Countries', fontsize=10, loc='lower right')

ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()