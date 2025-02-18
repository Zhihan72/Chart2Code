import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Growth of Electric Vehicle (EV) Adoption Over the Last Decade
years = np.arange(2010, 2021)
num_evs_sold = [2, 5, 15, 30, 55, 85, 150, 250, 450, 700, 1200]
charging_stations = [10, 30, 50, 90, 150, 240, 380, 550, 780, 950, 1300]

def growth_rate(data):
    rates = [0]
    for i in range(1, len(data)):
        rates.append((data[i] - data[i-1]) / data[i-1] * 100)
    return rates

# Growth rates for higher dimensional insights
ev_growth_rate = growth_rate(num_evs_sold)
charging_station_rate = growth_rate(charging_stations)

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot the number of EVs sold and number of charging stations on the primary y-axis
ax1.plot(years, num_evs_sold, color='blue', linestyle='-', linewidth=2, marker='o', label='EVs Sold (in thousands)')
ax1.plot(years, charging_stations, color='green', linestyle='--', linewidth=2, marker='s', label='Charging Stations')

# Customize grid and layout
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add a secondary y-axis for growth rates
ax2 = ax1.twinx()
ax2.plot(years, ev_growth_rate, color='red', linestyle='-', linewidth=1, marker='^', alpha=0.7, label='EV Growth Rate (%)')
ax2.plot(years, charging_station_rate, color='purple', linestyle=':', linewidth=1, marker='d', alpha=0.7, label='Charging Station Growth Rate (%)')

# Titles and labels
ax1.set_title('Decadal Rise in Electric Vehicle Adoption and Infrastructure Support (2010-2020)', fontsize=16, weight='bold')
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Numbers (in thousands)", fontsize=14)
ax2.set_ylabel("Growth Rate (%)", fontsize=14, color='black')

# Adding trend lines
z_evs = np.polyfit(years, num_evs_sold, 2)
p_evs = np.poly1d(z_evs)
ax1.plot(years, p_evs(years), color='blue', linestyle='-', alpha=0.3, linewidth=1)

z_stations = np.polyfit(years, charging_stations, 2)
p_stations = np.poly1d(z_stations)
ax1.plot(years, p_stations(years), color='green', linestyle='--', alpha=0.3, linewidth=1)

# Annotations and highlights
ax1.annotate('Significant increase in EV sales', xy=(2018, 450), xytext=(2015, 600),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, ha='center')

highlight_year = 2015
ax1.axvline(x=highlight_year, color='orange', linestyle='--', linewidth=1, alpha=0.8)
ax1.text(highlight_year + 0.1, 1000, 'Infrastructure Boost Year', color='orange', fontsize=12, rotation=90)

# Legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()