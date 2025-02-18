import matplotlib.pyplot as plt
import numpy as np

decades = np.array(['Early 80s', 'Mid 90s', 'Noughties', 'Teens', 'Twenties'])

vhs_usage = [80, 60, 20, 0, 0]
dvd_usage = [5, 60, 80, 40, 10]
bluray_usage = [0, 10, 50, 70, 45]
digital_usage = [0, 1, 10, 75, 90]
streaming_plus_usage = [0, 0, 0, 10, 40]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(decades, vhs_usage, marker='o', linestyle='-', linewidth=2, color='#800000')
ax.plot(decades, dvd_usage, marker='^', linestyle='--', linewidth=2, color='#1A237E')
ax.plot(decades, bluray_usage, marker='s', linestyle=':', linewidth=2, color='#388E3C')
ax.plot(decades, digital_usage, marker='D', linestyle='-.', linewidth=2, color='#D32F2F')
ax.plot(decades, streaming_plus_usage, marker='*', linestyle=(0, (3, 1, 1, 1)), linewidth=2, color='#FF8F00')

ax.set_title("Shifts in Media Dominance:\nVideotapes to Digital Streams", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Era', fontsize=12, fontweight='bold')
ax.set_ylabel('Popularity (%)', fontsize=12, fontweight='bold')

for spine in ax.spines.values():
    spine.set_visible(False)

plt.show()