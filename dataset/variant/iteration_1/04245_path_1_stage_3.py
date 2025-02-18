import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1960, 2020, 10)

dragons_n = [150, 180, 220, 260, 240, 200]
dragons_e = [100, 130, 180, 220, 260, 300]
dragons_w = [80, 90, 130, 170, 160, 150]

unicorns_n = [200, 210, 250, 280, 260, 240]
unicorns_e = [230, 270, 300, 310, 305, 290]
unicorns_w = [120, 150, 180, 210, 220, 230]

phoenixes_n = [50, 70, 90, 120, 150, 180]
phoenixes_e = [60, 80, 130, 170, 210, 250]
phoenixes_w = [40, 50, 60, 80, 110, 140]

def plot_creature(ax, years, data_n, data_e, data_w, creature):
    ax.plot(years, data_e, marker='o', label='East')
    ax.plot(years, data_w, marker='s', label='West')
    ax.plot(years, data_n, marker='^', label='North')
    ax.set_title(creature, fontsize=14)
    ax.set_xlabel('Yr', fontsize=12)
    ax.set_ylabel('Pop', fontsize=12)
    ax.legend()

fig, axes = plt.subplots(3, 1, figsize=(12, 18))

plot_creature(axes[0], years, dragons_n, dragons_e, dragons_w, 'Dragons')
plot_creature(axes[1], years, unicorns_n, unicorns_e, unicorns_w, 'Unicorns')
plot_creature(axes[2], years, phoenixes_n, phoenixes_e, phoenixes_w, 'Phoenixes')

fig.suptitle('Mythical Pop Trends (1970-2020)', fontsize=20, fontweight='bold', y=0.92)
plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()