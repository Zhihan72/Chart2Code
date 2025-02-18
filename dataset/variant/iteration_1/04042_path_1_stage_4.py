import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
                  2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
avg_temps = np.array([15.1, 15.3, 15.4, 15.7, 15.9, 16.0, 16.1, 16.3, 16.5, 16.6, 
                      16.8, 17.0, 17.1, 17.3, 17.5, 17.6, 17.8, 18.0, 18.1, 18.3, 18.5])
high_temps = np.array([25.3, 25.5, 25.7, 26.0, 26.2, 26.4, 26.6, 26.7, 26.9, 27.0, 
                       27.2, 27.4, 27.6, 27.7, 27.9, 28.0, 28.2, 28.4, 28.6, 28.7, 28.9])

fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(years, avg_temps, marker='o', linestyle='-', color='cyan')
ax.plot(years, high_temps, marker='s', linestyle='--', color='orange')

events = {
    2003: "Heatwave",
    2010: "Warm Winter",
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

ax.set_title('Temp Trends in Heatville (2000-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Temp (°C)', fontsize=14)

base_avg_temp = avg_temps[0]
anomalies = avg_temps - base_avg_temp
ax2 = ax.twinx()
ax2.plot(years, anomalies, color='darkgreen', marker='x', linestyle='-.')
ax2.set_ylabel('Temp Anomaly (°C)', fontsize=14, color='darkgreen')
ax2.tick_params(axis='y', labelcolor='darkgreen')

plt.tight_layout()
plt.show()