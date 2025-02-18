import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
avg_temp_greenland = np.array([-15, -14.8, -14.7, -14.5, -14.3, -14.1, -13.9, -13.5, 
                               -13.0, -12.8, -12.5, -12.2, -12.1, -11.9, -11.5, -11.2, 
                               -10.9, -10.5, -10.3, -10.1, -9.8])

plt.figure(figsize=(14, 8))

# Modified color and marker style
plt.plot(years, avg_temp_greenland, label='Mean Temperature (°C)', color='darkorange', linestyle='--', linewidth=2, marker='s')
plt.title('Greenland Temperature Trends:\nAnnual Analysis (2000-2020)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Calendar Year', fontsize=14)
plt.ylabel('Avg Temp in Celsius', fontsize=14)

# Changed the color and style of axhline
plt.axhline(y=-14, color='red', linestyle='-.', alpha=0.7, label=' -14 Celsius Reference')
plt.axvspan(2015, 2020, color='grey', alpha=0.3, label='Most Recent Period')

# Modified annotations and arrow style
for notable_year, annotation in zip([2004, 2010, 2016], ['Temperature Spike', 'Historic Ice Drop', 'Climate Phenomenon']):
    plt.annotate(annotation, xy=(notable_year, avg_temp_greenland[notable_year - 2000]), 
                 xytext=(notable_year, avg_temp_greenland[notable_year - 2000] + 0.5),
                 arrowprops=dict(facecolor='blue', arrowstyle='-|>'),
                 fontsize=12, color='purple')

# Adding grid
plt.grid(True, linestyle='--', linewidth=0.5)

plt.legend(loc='lower right', fontsize=12)
plt.tight_layout()
plt.show()