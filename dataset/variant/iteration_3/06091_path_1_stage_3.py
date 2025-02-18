import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1980, 1990, 2000, 2010, 2020])
key_point_1 = np.array([1500, 1200, 900, 800, 1100])
key_point_2 = np.array([3000, 2800, 2500, 2400, 3000])
key_point_4 = np.array([2000, 1800, 1500, 1400, 2000])
conservation_efforts = np.array([20, 40, 60, 80, 90])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(decades, key_point_1, 'o-', label='Route Alpha', color='green')
ax.plot(decades, key_point_2, 's-', label='Route Beta', color='green')
ax.plot(decades, key_point_4, 'd-', label='Route Gamma', color='green')

ax2 = ax.twinx()
ax2.plot(decades, conservation_efforts, 'o--', color='green', label='Efforts Impact')

ax.set_title('Butterfly Movement (1980-2020)\nSpotting & Conservation Trends', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Years', fontsize=12)
ax.set_ylabel('Butterfly Count', fontsize=12)
ax2.set_ylabel('Effort Efficiency (%)', fontsize=12, color='green')

ax.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

for decade, kp1, kp2, kp4 in zip(decades, key_point_1, key_point_2, key_point_4):
    ax.text(decade, kp1 + 100, f'{kp1}', ha='center', fontsize=9, color='green')
    ax.text(decade, kp2 + 100, f'{kp2}', ha='center', fontsize=9, color='green')
    ax.text(decade, kp4 + 100, f'{kp4}', ha='center', fontsize=9, color='green')

for decade, ce in zip(decades, conservation_efforts):
    ax2.text(decade, ce - 10, f'{ce}%', ha='center', fontsize=9, color='green')

plt.tight_layout()
plt.show()