import numpy as np
import matplotlib.pyplot as plt

decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

coal = [300, 400, 500, 600, 550, 400, 300]
oil = [200, 250, 300, 350, 400, 350, 200]
natural_gas = [100, 150, 200, 250, 300, 400, 500]
nuclear = [0, 50, 100, 150, 200, 250, 300]
renewables = [10, 20, 50, 100, 200, 400, 600]

# Additional fictional data series
hydrogen = [0, 0, 10, 20, 30, 50, 100]
geothermal = [5, 10, 15, 20, 30, 40, 50]

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(decades, coal, label='Coal', color='darkgrey', marker='D', linestyle='--', linewidth=1.5)
ax.plot(decades, oil, label='Oil', color='saddlebrown', marker='o', linestyle='-', linewidth=2.5)
ax.plot(decades, natural_gas, label='Natural Gas', color='cyan', marker='P', linestyle=':', linewidth=2)
ax.plot(decades, nuclear, label='Nuclear', color='orchid', marker='x', linestyle='-.', linewidth=1)
ax.plot(decades, renewables, label='Renewables', color='lime', marker='^', linestyle='-', linewidth=2)

# Plot new energy sources
ax.plot(decades, hydrogen, label='Hydrogen', color='blue', marker='s', linestyle='-', linewidth=2)
ax.plot(decades, geothermal, label='Geothermal', color='brown', marker='v', linestyle='-', linewidth=2)

ax.annotate('Oil Crisis', xy=('1970s', 250), xytext=('1980s', 350),
            arrowprops=dict(facecolor='gray', arrowstyle='->', lw=2), fontsize=10, color='maroon')
ax.annotate('Rise of Renewables', xy=('2010s', 400), xytext=('2000s', 300),
            arrowprops=dict(facecolor='green', arrowstyle='->', lw=2), fontsize=10, color='darkgreen')

ax.set_title('Energy Consumption Trends:\nThe Evolution of Energy Sources', fontsize=17, fontweight='bold', pad=15)
ax.set_xlabel('Decades', fontsize=13)
ax.set_ylabel('Energy Consumption (TW)', fontsize=13)
ax.legend(loc='upper right', fontsize=10, title='Energy Sources', frameon=True, facecolor='lightyellow', edgecolor='grey')

ax.grid(True, linestyle='-', alpha=0.3)

plt.xticks(rotation=30)
plt.yticks(np.arange(0, 701, 100))

plt.tight_layout()
plt.show()