import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2023)

city_A_temps = [16.2, 18.1, 17.0, 16.5, 19.8, 17.3, 18.4, 18.7, 17.7, 20.5, 19.1, 20.2, 19.5]
city_B_temps = [17.8, 14.4, 14.0, 15.1, 16.4, 14.7, 18.2, 16.1, 15.8, 17.5, 16.8, 17.1, 15.4]
city_C_temps = [12.2, 14.0, 10.8, 13.6, 14.3, 11.5, 12.6, 12.9, 11.9, 10.5, 14.7, 11.2, 13.3]

fig, ax = plt.subplots(figsize=(14, 8))

# Stylistic changes
ax.plot(years, city_A_temps, marker='D', linestyle='-', color='#1f77b4', linewidth=2, label='A')
ax.plot(years, city_B_temps, marker='x', linestyle=':', color='#ff7f0e', linewidth=2, label='B')
ax.plot(years, city_C_temps, marker='+', linestyle='--', color='#2ca02c', linewidth=2, label='C')

ax.set_title('Temp Rise\n2010-2022', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Avg Temp (°C)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.legend(title='City', loc='lower right', fontsize=10)

annotations = {
    2015: ("Mid-Decade", city_A_temps[5]),
    2018: ("Spike", city_B_temps[8]),
    2022: ("Inc.", city_C_temps[12]),
}

for year, (text, y_value) in annotations.items():
    ax.annotate(text, xy=(year, y_value), xytext=(year, y_value + 1),
                arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=5), fontsize=10, color='blue', ha='center')

ax.grid(True, linestyle='-.', alpha=0.7)

plt.tight_layout()

plt.show()