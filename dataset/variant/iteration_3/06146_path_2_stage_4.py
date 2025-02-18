import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
num_evs_sold = [15, 5, 30, 2, 55, 150, 250, 85, 450, 1200, 700]  # Shuffled values
charging_stations = [10, 90, 50, 240, 780, 150, 380, 550, 1300, 950, 30]  # Shuffled values

def growth_rate(data):
    rates = [0]
    for i in range(1, len(data)):
        rates.append((data[i] - data[i-1]) / data[i-1] * 100)
    return rates

ev_growth_rate = growth_rate(num_evs_sold)
charging_station_rate = growth_rate(charging_stations)

fig, ax1 = plt.subplots(figsize=(14, 9))

# Shuffled color assignments
ax1.plot(years, num_evs_sold, color='purple', linestyle='-', linewidth=2, marker='o')
ax1.plot(years, charging_stations, color='red', linestyle='--', linewidth=2, marker='s')

ax2 = ax1.twinx()
ax2.plot(years, ev_growth_rate, color='green', linestyle='-', linewidth=1, marker='^', alpha=0.7)
ax2.plot(years, charging_station_rate, color='blue', linestyle=':', linewidth=1, marker='d', alpha=0.7)

ax1.set_title('Electric Phenomenon and Charging Evolution (2010-2020)', fontsize=16, weight='bold')
ax1.set_xlabel("Timeline", fontsize=14)
ax1.set_ylabel("Volume (x1000)", fontsize=14)
ax2.set_ylabel("Rate of Change (%)", fontsize=14, color='black')

# Shuffled color assignments for polynomial fits
z_evs = np.polyfit(years, num_evs_sold, 2)
p_evs = np.poly1d(z_evs)
ax1.plot(years, p_evs(years), color='purple', linestyle='-', alpha=0.3, linewidth=1)

z_stations = np.polyfit(years, charging_stations, 2)
p_stations = np.poly1d(z_stations)
ax1.plot(years, p_stations(years), color='red', linestyle='--', alpha=0.3, linewidth=1)

ax1.annotate('Noticeable EV Surge', xy=(2018, 450), xytext=(2015, 600),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, ha='center')

highlight_year = 2015
ax1.axvline(x=highlight_year, color='orange', linestyle='--', linewidth=1, alpha=0.8)
ax1.text(highlight_year + 0.1, 1000, 'Year of Charge', color='orange', fontsize=12, rotation=90)

plt.tight_layout()
plt.show()