import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
consumption_current_year = np.array([160, 155, 140, 150, 200, 170, 190, 220, 210, 180, 165, 175])
consumption_previous_year = np.array([150, 145, 165, 138, 160, 195, 185, 215, 205, 175, 160, 170])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, consumption_current_year, marker='o', markersize=8, linestyle='-', color='orange')
ax.plot(months, consumption_previous_year, marker='s', markersize=8, linestyle='--', color='purple')

for spine in ax.spines.values():
    spine.set_visible(False)

peak_current = months[np.argmax(consumption_current_year)]
peak_previous = months[np.argmax(consumption_previous_year)]
ax.annotate('', 
            xy=(peak_current, max(consumption_current_year)), 
            xytext=(peak_current, max(consumption_current_year) + 20),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('', 
            xy=(peak_previous, max(consumption_previous_year)), 
            xytext=(peak_previous, max(consumption_previous_year) + 20),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()