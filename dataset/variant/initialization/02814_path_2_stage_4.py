import matplotlib.pyplot as plt
import numpy as np

decades = ['70s', '80s', '90s', '00s', '10s']

solar_energy = np.array([
    [5, 10, 15, 20, 25]  # Harmony
])
wind_energy = np.array([
    [10, 12, 15, 20, 30]  # Harmony
])

fig, ax = plt.subplots(figsize=(12, 8))

new_solar_color = '#FF6347'  # Tomato
new_wind_color = '#76EE00'  # Chartreuse

ax.fill_between(decades, solar_energy[0], color=new_solar_color, alpha=0.6)
ax.fill_between(decades, wind_energy[0], color=new_wind_color, alpha=0.6)

ax.plot(decades, solar_energy[0], color=new_solar_color, linewidth=2)
ax.plot(decades, wind_energy[0], color=new_wind_color, linewidth=2)

ax.set_title("Energy in Harmony", fontsize=16, fontweight='bold')
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Usage (Units)', fontsize=12)

ax.set_xticks(decades)

# Remove borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()