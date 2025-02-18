import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
ev_sales = [1, 3, 5, 9, 14, 20, 27, 35, 44, 54, 65]
charging_stations = [50, 70, 100, 150, 220, 300, 400, 520, 660, 820, 1000]
renewable_growth = [10, 15, 20, 26, 33, 41, 50, 60, 71, 83, 96]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Randomly change marker types and line styles
ax1.plot(years, ev_sales, color='blue', marker='x', linestyle='-', linewidth=2, label='EV Sales (millions)')
ax1.set_title("Adoption of Electric Vehicles, Charging Infrastructure Growth, and Renewable Energy Uptake (2020-2030)",
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("EV Sales (millions)", fontsize=14, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(years, charging_stations, color='green', marker='d', linestyle='-', linewidth=2, label='Charging Stations (thousands)')
ax2.set_ylabel("Charging Stations (thousands)", fontsize=14, color='green')
ax2.tick_params(axis='y', labelcolor='green')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(years, renewable_growth, color='orange', marker='p', linestyle=':', linewidth=2, label='Renewable Energy (%)')
ax3.set_ylabel("Renewable Energy (%)", fontsize=14, color='orange')
ax3.tick_params(axis='y', labelcolor='orange')

# Change grid style
ax1.grid(True, linestyle='-.', alpha=0.5)

# Modify legend properties
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
lines_3, labels_3 = ax3.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2 + lines_3, labels_1 + labels_2 + labels_3, loc='upper right', fontsize=12, frameon=False)

# Modify border (spine) visibility
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax3.spines['top'].set_visible(False)

# Adjust annotation
ax1.annotate(f'{ev_sales[0]}M', xy=(2020, ev_sales[0]), xytext=(2020, ev_sales[0] + 2),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkblue')

ax1.annotate(f'{ev_sales[-1]}M', xy=(2030, ev_sales[-1]), xytext=(2029.5, ev_sales[-1] - 8),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkred')

ax2.annotate(f'{charging_stations[0]}K', xy=(2020, charging_stations[0]), xytext=(2020.5, charging_stations[0] + 50),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkgreen')

ax2.annotate(f'{charging_stations[-1]}K', xy=(2030, charging_stations[-1]), xytext=(2029, charging_stations[-1] - 200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkgreen')

ax3.annotate(f'{renewable_growth[0]}%', xy=(2020, renewable_growth[0]), xytext=(2020, renewable_growth[0] + 5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkorange')

ax3.annotate(f'{renewable_growth[-1]}%', xy=(2030, renewable_growth[-1]), xytext=(2029.5, renewable_growth[-1] - 10),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkorange')

plt.tight_layout()
plt.show()