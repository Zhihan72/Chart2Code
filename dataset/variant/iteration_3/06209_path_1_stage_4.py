import matplotlib.pyplot as plt
import numpy as np

# Days
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
x = np.arange(len(days))

# Data: Screen time
screen_time = [3, 4, 4.5, 5, 6, 7, 5.5]

fig, ax1 = plt.subplots(figsize=(12, 6))

# Consistent color for screen time
color = 'blue'

# Screen time
ax1.set_xlabel('Day', fontsize=12, fontweight='bold')
ax1.set_ylabel('Screen Time (hrs)', color=color, fontsize=12, fontweight='bold')
ax1.plot(days, screen_time, color=color, marker='D', linestyle=':', linewidth=3, label='Screen Time')
ax1.tick_params(axis='y', labelcolor=color)

# Title
plt.title('Screen Time over a Week', fontsize=16, fontweight='bold', pad=10)

# Legend
ax1.legend(loc='upper right', fontsize=9, frameon=False)

# Border
for spine in ax1.spines.values():
    spine.set_linewidth(1.5)

# Display
plt.show()