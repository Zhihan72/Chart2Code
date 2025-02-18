import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)
public_transport = np.array([30, 32, 34, 35, 36, 38, 40, 42, 45, 48, 50])
cycling = np.array([6, 7, 8, 9, 12, 14, 13, 15, 21, 20, 24])
walking = np.array([11, 10, 13, 14, 13, 16, 14, 18, 17, 20, 22])
electric_vehicles = np.array([2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20])
conventional_vehicles = np.array([51, 48, 41, 37, 33, 26, 23, 11, 2, 1, 0])
sustainable_transport = cycling + walking + electric_vehicles

fig, ax = plt.subplots(figsize=(14, 9))

ax.bar(years, public_transport, color='#4d88ff')
ax.bar(years, cycling, bottom=public_transport, color='#ff9933')
ax.bar(years, walking, bottom=public_transport + cycling, color='#66c266')
ax.bar(years, electric_vehicles, bottom=public_transport + cycling + walking, color='#cc66ff')
ax.bar(years, conventional_vehicles, bottom=public_transport + cycling + walking + electric_vehicles, color='#ff6666')

ax.plot(years, sustainable_transport, color='gold', linewidth=2.5, marker='o', markersize=8)

ax.set_title("Urban Transport Modes (2012-2022)", fontsize=16, fontweight='bold', loc='left')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("%", fontsize=12)
ax.set_xticks(years)
ax.set_yticks(range(0, 101, 10))
ax.set_ylim(0, 100)

def annotate_bars(containers):
    for container in containers:  # Iterate over bar containers
        for bar in container:  # Iterate over individual bars within the container
            height = bar.get_height()
            if height > 0:
                ax.annotate(f'{height}%', 
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3),  # Offset slightly above the bar
                            textcoords='offset points',
                            ha='center', va='bottom',
                            fontsize=9, color='black', weight='bold')

annotate_bars(ax.containers)

for (x, y) in zip(years, sustainable_transport):
    ax.annotate(f'{y}%', xy=(x, y), xytext=(-10, 10), textcoords='offset points',
                fontsize=10, color='darkgoldenrod', weight='bold',
                arrowprops=dict(arrowstyle="->", color='darkgoldenrod', lw=1))

# Remove all borders
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()