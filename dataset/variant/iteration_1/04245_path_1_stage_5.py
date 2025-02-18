import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1960, 2020, 10)

# Changed data values slightly while maintaining the structure
dragons_n = [180, 200, 220, 260, 250, 210]  # Altered some values for first data group
dragons_e = [100, 130, 180, 230, 260, 290]  # Altered some values for second data group
dragons_w = [90, 110, 140, 180, 150, 140]   # Altered some values for third data group

unicorns_n = [240, 220, 230, 270, 250, 230]  # Slight alterations for another creature group
unicorns_e = [230, 280, 295, 315, 300, 275]  # Small changes preserving the order
unicorns_w = [130, 160, 170, 205, 215, 225]  # Another random shuffle within the structure

def plot_creature(ax, years, data_n, data_e, data_w, creature):
    ax.plot(years, data_e, marker='o', label='East')
    ax.plot(years, data_w, marker='s', label='West')
    ax.plot(years, data_n, marker='^', label='North')
    ax.set_title(creature, fontsize=14)
    ax.set_xlabel('Yr', fontsize=12)
    ax.set_ylabel('Pop', fontsize=12)
    ax.legend()

fig, axes = plt.subplots(2, 1, figsize=(12, 12))

plot_creature(axes[0], years, dragons_n, dragons_e, dragons_w, 'Dragons')
plot_creature(axes[1], years, unicorns_n, unicorns_e, unicorns_w, 'Unicorns')

fig.suptitle('Mythical Pop Trends (1970-2020)', fontsize=20, fontweight='bold', y=0.92)
plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()