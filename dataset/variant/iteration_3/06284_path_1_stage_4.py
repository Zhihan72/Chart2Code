import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperatures = [18.0, 16.1, 15.4, 27.5, 23.2, 20.5, 15.0, 27.0, 18.3, 21.2, 25.3, 25.7]
rainfall = [20, 110, 18, 55, 60, 78, 42, 40, 30, 90, 25, 120]

fig, ax1 = plt.subplots(figsize=(12, 8))

consistent_color = 'tab:blue'

ax1.plot(months, temperatures, color=consistent_color, marker='x', linestyle='-.', linewidth=2.5)
ax1.tick_params(axis='y', labelcolor=consistent_color)

ax2 = ax1.twinx()

ax2.plot(months, rainfall, color=consistent_color, marker='d', linestyle='-', linewidth=1.5)
ax2.tick_params(axis='y', labelcolor=consistent_color)
ax2.grid(axis='y', linestyle='-', color='gray', alpha=0.4)

plt.tight_layout()
plt.show()