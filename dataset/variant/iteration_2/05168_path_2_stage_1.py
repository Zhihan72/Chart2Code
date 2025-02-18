import matplotlib.pyplot as plt
import numpy as np

# Title and axis labels
title = "Temp Variation"
x_label = "Days"
y_label = "Temp (°F)"

# Days of the week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Temperature data for three cities
new_york_temp = [55, 60, 58, 62, 65, 63, 61]          
san_francisco_temp = [50, 52, 54, 53, 55, 56, 57]    
miami_temp = [75, 77, 76, 78, 80, 81, 82]            

fig, ax = plt.subplots(figsize=(10, 6))

# Plot the temperature data
ax.plot(days, new_york_temp, marker='o', linestyle='-', color='b', label='NY')
ax.plot(days, san_francisco_temp, marker='s', linestyle='--', color='g', label='SF')
ax.plot(days, miami_temp, marker='^', linestyle=':', color='r', label='MIA')

# Title and labels
plt.title(title, fontsize=16, fontweight='bold')
plt.xlabel(x_label, fontsize=14)
plt.ylabel(y_label, fontsize=14)

# Grid and legend
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(loc='upper left', fontsize=12, title="Cities", title_fontsize='13')

# Annotating highest temperature in Miami
max_temp_miami = max(miami_temp)
max_temp_day = days[miami_temp.index(max_temp_miami)]
plt.annotate(f'Highest: {max_temp_miami}°F',
             xy=(max_temp_day, max_temp_miami),
             xytext=(max_temp_day, max_temp_miami + 5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))

plt.tight_layout()

plt.show()