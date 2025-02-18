import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2051)
num_space_tourists = [
    0, 1, 5, 12, 22, 36, 50, 65, 80, 100, 120, 140, 
    165, 190, 220, 250, 285, 320, 360, 400, 450, 
    500, 560, 620, 690, 770 
]

fig, ax1 = plt.subplots(figsize=(12, 8))

color1 = 'darkorange'
ax1.set_xlabel('Yr')
ax1.set_ylabel('Tourists', color=color1)
ax1.plot(years, num_space_tourists, color=color1, linewidth=2.5, marker='o')
ax1.tick_params(axis='y', labelcolor=color1)

ax1.set_title('Space Tourism (2025-2050)', fontsize=14, fontweight='bold', pad=10)

milestones_tourists = {
    2030: 'First Hotel',
    2045: 'Interplanetary Tours'
}
for year, annotation in milestones_tourists.items():
    idx = years.tolist().index(year)
    tourists_val = num_space_tourists[idx]
    ax1.annotate(annotation, xy=(year, tourists_val), xytext=(year, tourists_val + 50),
                 arrowprops=dict(facecolor='darkorange', arrowstyle='->'), fontsize=10, ha='center', color='darkorange')

plt.show()