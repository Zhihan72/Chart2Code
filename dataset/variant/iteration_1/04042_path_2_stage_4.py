import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
                  2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
avg_temps = np.array([15.9, 16.0, 15.4, 17.8, 16.5, 18.1, 16.1, 18.3, 16.6, 15.7, 
                      16.3, 17.1, 15.1, 17.3, 17.0, 17.5, 18.5, 15.3, 17.6, 18.0, 16.8])
high_temps = np.array([26.4, 28.7, 27.2, 26.6, 27.9, 25.5, 28.2, 27.4, 25.3, 27.7, 
                       28.0, 25.7, 27.6, 28.9, 28.4, 26.0, 26.9, 28.6, 26.2, 26.7, 27.0])
low_temps = np.array([6.8, 7.1, 8.0, 6.5, 7.4, 7.6, 5.6, 8.5, 7.7, 7.3, 5.7, 7.2, 
                      8.3, 8.2, 6.1, 5.9, 5.8, 6.9, 7.8, 5.9, 6.7])

fig, ax = plt.subplots(figsize=(14, 7))

consistent_color = 'royalblue'

ax.plot(years, avg_temps, marker='o', linestyle='-', color=consistent_color)
ax.plot(years, high_temps, marker='s', linestyle='--', color=consistent_color)
ax.plot(years, low_temps, marker='v', linestyle=':', color=consistent_color)

events = {
    2003: "Heatwave Event",
    2010: "Warmest Winter",
    2018: "Hot Summer"
}

for year, event in events.items():
    temp = avg_temps[years.tolist().index(year)]
    ax.annotate(event,
                xy=(year, temp),
                xytext=(year, temp + 1),
                arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=5),
                fontsize=10,
                color='darkred')

ax.set_title('Annual Weather Trend in HotCity (2000-2020)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Calendar Year', fontsize=14)
ax.set_ylabel('Degrees Celsius', fontsize=14)

# Remove grid
ax.grid(False)

# Remove border by hiding spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

base_avg_temp = avg_temps[0]
anomalies = avg_temps - base_avg_temp
ax2 = ax.twinx()
ax2.plot(years, anomalies, color=consistent_color, marker='x', linestyle='-.')
ax2.set_ylabel('Anomaly (°C)', fontsize=14, color=consistent_color)
ax2.tick_params(axis='y', labelcolor=consistent_color)

plt.tight_layout()
plt.show()