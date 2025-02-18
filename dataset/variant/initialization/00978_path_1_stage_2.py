import matplotlib.pyplot as plt
import numpy as np

# Years of interest
years = np.arange(2012, 2023)

# Mode of transport percentages over the years
public_transport = np.array([30, 32, 34, 35, 36, 38, 40, 42, 45, 48, 50])
cycling = np.array([6, 7, 8, 9, 12, 14, 13, 15, 21, 20, 24])
walking = np.array([11, 10, 13, 14, 13, 16, 14, 18, 17, 20, 22])
electric_vehicles = np.array([2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20])
conventional_vehicles = np.array([51, 48, 41, 37, 33, 26, 23, 11, 2, 1, 0])

# Recompute the total sustainable transport usage for visualization purposes
sustainable_transport = cycling + walking + electric_vehicles

fig, ax = plt.subplots(figsize=(14, 9))

bars1 = ax.bar(years, public_transport, label='Public', color='#4d88ff')
bars2 = ax.bar(years, cycling, bottom=public_transport, label='Cycling', color='#ff9933')
bars3 = ax.bar(years, walking, bottom=public_transport + cycling, label='Walking', color='#66c266')
bars4 = ax.bar(years, electric_vehicles, bottom=public_transport + cycling + walking,
               label='EVs', color='#cc66ff')
bars5 = ax.bar(years, conventional_vehicles, bottom=public_transport + cycling + walking + electric_vehicles,
               label='Conventional', color='#ff6666')

ax.plot(years, sustainable_transport, label='Sustainable Total', color='gold', linewidth=2.5, marker='o', markersize=8)

ax.set_title("Urban Transport Modes (2012-2022)", fontsize=16, fontweight='bold', loc='left')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("%", fontsize=12)
ax.set_xticks(years)
ax.set_yticks(range(0, 101, 10))
ax.set_ylim(0, 100)

def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.annotate(f'{height}%', 
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                        xytext=(0, 0), 
                        textcoords='offset points',
                        ha='center', va='center',
                        fontsize=9, color='black', weight='bold')

annotate_bars(bars1)
annotate_bars(bars2)
annotate_bars(bars3)
annotate_bars(bars4)
annotate_bars(bars5)

for (x, y) in zip(years, sustainable_transport):
    ax.annotate(f'{y}%', xy=(x, y), xytext=(-10, 10), textcoords='offset points',
                fontsize=10, color='darkgoldenrod', weight='bold',
                arrowprops=dict(arrowstyle="->", color='darkgoldenrod', lw=1))

ax.legend(title="Transport Mode", loc='upper right', bbox_to_anchor=(1.2, 1))

ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

plt.show()