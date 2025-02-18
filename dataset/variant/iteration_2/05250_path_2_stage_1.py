import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
gdp_growth = np.array([2.3, 2.6, 2.7, 2.9, 3.0, 3.2, 3.1, 2.8, 2.5, 2.0, 1.8])
unemployment_rate = np.array([7.8, 7.5, 7.2, 7.0, 6.8, 6.7, 6.6, 6.5, 6.3, 6.2, 6.1])
inflation_rate = np.array([1.5, 1.7, 1.8, 2.0, 2.2, 2.5, 2.4, 2.3, 2.1, 1.9, 1.8])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot GDP Growth
ax1.plot(years, gdp_growth, label='GDP Growth (%)', color='magenta', marker='x', linestyle='--', linewidth=2, markersize=8)
# Plot Unemployment Rate
ax1.plot(years, unemployment_rate, label='Unemployment Rate (%)', color='cyan', marker='D', linestyle='-.', linewidth=3, markersize=8)
# Plot Inflation Rate
ax1.plot(years, inflation_rate, label='Inflation Rate (%)', color='orange', marker='v', linestyle=':', linewidth=1, markersize=10)

ax1.set_title("Economic Indicators in Imaginaryland (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Percentage (%)", fontsize=12)

# Annotating key events
key_events = {
    2012: ("Fiscal Policy\nOverhaul", 8.1, 8.0),
    2015: ("Energy Crisis\nMitigation", 7.0, 1.5),
    2018: ("Tech Boom Start", 6.6, 2.4),
}

for year, (event, y_gdp, y_unemployment) in key_events.items():
    ax1.annotate(event, xy=(year, y_gdp),
                 xytext=(year, y_gdp + 0.5),
                 textcoords='data',
                 arrowprops=dict(arrowstyle='->', color='grey'),
                 ha='center', fontsize=10, color='black')

# Adjusting grid style
ax1.grid(True, linestyle=':', linewidth=0.7, alpha=0.9)

# Alter legend position
ax1.legend(loc='upper left', fontsize=12)

ax1.set_xticks(years)
plt.xticks(rotation=60)
plt.tight_layout()

plt.show()