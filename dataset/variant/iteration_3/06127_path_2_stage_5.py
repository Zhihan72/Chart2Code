import matplotlib.pyplot as plt
import numpy as np

hours_range = ['0-3', '4-5', '6-7', '8-9', '10-11', '12+']
weekday_sleepers = [5, 15, 40, 80, 30, 10]

y_pos = np.arange(len(hours_range))

fig, ax = plt.subplots(figsize=(10, 6))

bar_height = 0.4

# Style changes: new color and random edgecolor, added hatch pattern
new_color_weekday = '#FF5722'  # Changed color
edge_color = 'blue'  # Changed edge color
hatch_pattern = '/'  # Added hatch pattern to bars

bars1 = ax.barh(y_pos, weekday_sleepers, bar_height, color=new_color_weekday, 
                edgecolor=edge_color, alpha=0.7, hatch=hatch_pattern)

# Restored y-tick labels
ax.set_yticks(y_pos)
ax.set_yticklabels(hours_range)

# Grid style changes: Randomly chose solid linestyle
ax.xaxis.grid(True, linestyle='-', alpha=0.9)  # Changed to solid line and adjusted alpha

# Adding a legend with a random position
ax.legend(['Weekday Sleepers'], loc='lower right')  # Added a legend

# Adding random border settings
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(0)  # Turned off the right spine

plt.tight_layout()
plt.show()