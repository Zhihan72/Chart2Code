import matplotlib.pyplot as plt
import numpy as np

regions = ['N', 'S']
years = ['2019', '2020', '2021', '2022']

north_generation = np.array([20, 25, 30, 35])
south_generation = np.array([25, 30, 35, 40])

north_diverging = north_generation
south_diverging = -south_generation

colors = ['#3498db', '#e74c3c']

fig, ax = plt.subplots(figsize=(12, 6))
x = np.arange(len(years))

ax.barh(x, north_diverging, color=colors[0], label='N', edgecolor='black')
ax.barh(x, south_diverging, color=colors[1], label='S', edgecolor='black')

ax.set_xlabel('Generation (GWh)', fontsize=12)
ax.set_title('Solar Power by Region', fontsize=16, fontweight='bold')
ax.set_yticks(x)
ax.set_yticklabels(years)
ax.legend(loc='upper right')

for i, (n, s) in enumerate(zip(north_diverging, south_diverging)):
    ax.text(n + 1, i, f'{n}', va='center', fontsize=10)
    ax.text(s - 1, i, f'{-s}', va='center', fontsize=10, ha='right')

ax.axvline(0, color='grey', linewidth=0.8)

plt.show()