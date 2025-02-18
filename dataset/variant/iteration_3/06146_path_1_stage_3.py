import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2021)
num_evs_sold = [2, 5, 15, 30, 55, 85, 150, 250, 450, 700, 1200]
charging_stations = [10, 30, 50, 90, 150, 240, 380, 550, 780, 950, 1300]
ev_models = [1, 2, 4, 6, 10, 13, 20, 30, 50, 80, 120]

def growth_rate(data):
    rates = [0]
    for i in range(1, len(data)):
        rates.append((data[i] - data[i-1]) / data[i-1] * 100)
    return rates

# Growth rates
ev_growth_rate = growth_rate(num_evs_sold)
charging_station_rate = growth_rate(charging_stations)
model_growth_rate = growth_rate(ev_models)

fig, ax1 = plt.subplots(figsize=(14, 9))

ax1.plot(years, num_evs_sold, color='blue', linestyle='-', linewidth=2, marker='o')
ax1.plot(years, charging_stations, color='green', linestyle='--', linewidth=2, marker='s')
ax1.plot(years, ev_models, color='brown', linestyle=':', linewidth=2, marker='x')

ax2 = ax1.twinx()
ax2.plot(years, ev_growth_rate, color='red', linestyle='-', linewidth=1, marker='^', alpha=0.7)
ax2.plot(years, charging_station_rate, color='purple', linestyle=':', linewidth=1, marker='d', alpha=0.7)
ax2.plot(years, model_growth_rate, color='orange', linestyle='-.', linewidth=1, marker='*', alpha=0.7)

# Altered Titles and labels
ax1.set_title('EV Revolution: A Decade of Change (2010-2020)', fontsize=16, weight='bold')
ax1.set_xlabel("Time Period", fontsize=14)
ax1.set_ylabel("Count (Thousands)", fontsize=14)
ax2.set_ylabel("Increment Rate (%)", fontsize=14)

z_evs = np.polyfit(years, num_evs_sold, 2)
p_evs = np.poly1d(z_evs)
ax1.plot(years, p_evs(years), color='blue', linestyle='-', alpha=0.3, linewidth=1)

z_stations = np.polyfit(years, charging_stations, 2)
p_stations = np.poly1d(z_stations)
ax1.plot(years, p_stations(years), color='green', linestyle='--', alpha=0.3, linewidth=1)

z_models = np.polyfit(years, ev_models, 2)
p_models = np.poly1d(z_models)
ax1.plot(years, p_models(years), color='brown', linestyle=':', alpha=0.3, linewidth=1)

# Modified Annotations and highlights
ax1.annotate('Boom in EV Sales', xy=(2018, 450), xytext=(2015, 600),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, ha='center')

highlight_year = 2015
ax1.axvline(x=highlight_year, color='orange', linestyle='--', linewidth=1, alpha=0.8)
ax1.text(highlight_year + 0.1, 1000, 'Critical Year for Growth', color='orange', fontsize=12, rotation=90)

plt.show()