import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

city_a = np.array([80, 70, 75, 60, 55, 65, 85, 90, 70, 80, 95, 100])
city_b = np.array([90, 80, 85, 75, 65, 75, 95, 100, 90, 95, 110, 105])
city_c = np.array([60, 55, 50, 45, 50, 55, 65, 70, 60, 65, 70, 75])
city_d = np.array([50, 45, 55, 50, 60, 70, 80, 85, 75, 80, 85, 90])
city_e = np.array([100, 95, 105, 95, 80, 85, 90, 95, 110, 115, 120, 125])

data = np.vstack([city_a, city_b, city_c, city_d, city_e])

fig, ax = plt.subplots(figsize=(12, 8))

# Changing stackplot visualization using different line styles
lines = [ax.plot(months, city, linestyle=style, linewidth=2)[0] for city, style in zip(data, ['-', '--', '-.', ':'])]

# Updating the color fill via stackplot
ax.stackplot(months, data, colors=['#184c83', '#df6b31', '#299c4a', '#a92320', '#6f579b'], alpha=0.5)

# Title and labels
ax.set_title("Monthly Rainfall\nfor Cities", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Months", fontsize=12, weight='bold')
ax.set_ylabel("Rain (mm)", fontsize=12, weight='bold')

# Change legend to be more integrated within the plot
ax.legend(['A', 'B', 'C', 'D', 'E'], loc='center left', title='Cities', fontsize=10)

# Altering grid to be dotted
ax.grid(True, which='both', linestyle=':', linewidth=0.75, alpha=0.5)

# Formatter
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, fontsize=10, rotation=45)
ax.set_yticks(np.arange(0, 151, 50))
ax.set_yticklabels(np.arange(0, 151, 50), fontsize=10)

plt.tight_layout()

plt.show()