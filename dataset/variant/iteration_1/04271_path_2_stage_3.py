import matplotlib.pyplot as plt
import numpy as np

days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

children_steps = np.array([15000, 16000, 15500, 15000, 14800, 17000, 18000])
adults_steps = np.array([10000, 10500, 10200, 9800, 9500, 11000, 11500])
elderly_steps = np.array([7000, 7200, 7100, 7000, 6800, 7300, 7500])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(days, children_steps, marker='o', linestyle='-', linewidth=2, color='#E377C2')
ax.plot(days, adults_steps, marker='s', linestyle='--', linewidth=2, color='#17BECF')
ax.plot(days, elderly_steps, marker='^', linestyle='-.', linewidth=2, color='#BCBD22')

ax.set_title("Weekly Steps by Age", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Day", fontsize=14)
ax.set_ylabel("Steps", fontsize=14)

peak_children = np.max(children_steps)
peak_adults = np.max(adults_steps)
peak_elderly = np.max(elderly_steps)

ax.annotate('Peak', xy=('Sun', peak_children), xytext=('Sat', peak_children + 1000),
            arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='darkred')
ax.annotate('Peak', xy=('Sun', peak_adults), xytext=('Sat', peak_adults + 500),
            arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='darkgreen')
ax.annotate('Peak', xy=('Sun', peak_elderly), xytext=('Sat', peak_elderly + 500),
            arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10, color='darkblue')

plt.tight_layout()
plt.show()