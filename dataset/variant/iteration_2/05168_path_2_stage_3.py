import matplotlib.pyplot as plt
import numpy as np

title = "Temp Variation"
x_label = "Days"
y_label = "Temp (°F)"

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

new_york_temp = [55, 60, 58, 62, 65, 63, 61]          
san_francisco_temp = [50, 52, 54, 53, 55, 56, 57]    
miami_temp = [75, 77, 76, 78, 80, 81, 82]            

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(days, new_york_temp, marker='*', linestyle='-.', color='g', label='NY')
ax.plot(days, san_francisco_temp, marker='D', linestyle='-', color='m', label='SF')
ax.plot(days, miami_temp, marker='x', linestyle='--', color='c', label='MIA')

plt.title(title, fontsize=16, fontweight='bold')
plt.xlabel(x_label, fontsize=14)
plt.ylabel(y_label, fontsize=14)

plt.grid(True, linestyle='-', linewidth=0.3)
plt.legend(loc='lower right', fontsize=10, title="City Temperatures", title_fontsize='11')

max_temp_miami = max(miami_temp)
max_temp_day = days[miami_temp.index(max_temp_miami)]
plt.annotate(f'Highest: {max_temp_miami}°F',
             xy=(max_temp_day, max_temp_miami),
             xytext=(max_temp_day, max_temp_miami + 5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))

ax.spines['top'].set_color('red')
ax.spines['right'].set_color('red')
ax.spines['left'].set_color('blue')
ax.spines['bottom'].set_color('blue')

plt.tight_layout()

plt.show()