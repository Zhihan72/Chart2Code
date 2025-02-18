import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
ev_sales = [1, 3, 6, 8, 15, 19, 28, 34, 45, 55, 63]
charging_stations = [45, 75, 95, 155, 210, 310, 390, 530, 650, 810, 995]

fig, ax1 = plt.subplots(figsize=(14, 8))
# Apply a single color to both plots
common_color = 'purple'

ax1.plot(years, ev_sales, color=common_color, marker='o', linewidth=2)

ax1.set_xlabel("Timeline", fontsize=14)
ax1.set_ylabel("EV Units Sold (millions)", fontsize=14, color=common_color)
ax1.tick_params(axis='y', labelcolor=common_color)

ax2 = ax1.twinx()
ax2.plot(years, charging_stations, color=common_color, marker='s', linestyle='--', linewidth=2)
ax2.set_ylabel("Stations (thousands)", fontsize=14, color=common_color)
ax2.tick_params(axis='y', labelcolor=common_color)

ax1.annotate(f'Init {ev_sales[0]}M', xy=(2020, ev_sales[0]), xytext=(2020, ev_sales[0] + 2),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkblue')

ax1.annotate(f'End {ev_sales[-1]}M', xy=(2030, ev_sales[-1]), xytext=(2029.5, ev_sales[-1] - 8),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkred')

ax2.annotate(f'Start {charging_stations[0]}K', xy=(2020, charging_stations[0]), xytext=(2020.5, charging_stations[0] + 50),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkgreen')

ax2.annotate(f'Peak {charging_stations[-1]}K', xy=(2030, charging_stations[-1]), xytext=(2029, charging_stations[-1] - 200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkgreen')

plt.tight_layout()
plt.show()