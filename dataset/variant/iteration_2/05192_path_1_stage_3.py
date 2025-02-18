import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)

# Revenue data (in billions USD)
ai_revenue = [6, 9, 12, 18, 25, 40]
cybersecurity_revenue = [15, 18, 20, 23, 30, 45]
blockchain_revenue = [1, 2, 3, 6, 9, 12]
cloud_revenue = [5, 8, 15, 22, 30, 50]

data = np.array([ai_revenue, cybersecurity_revenue, blockchain_revenue, cloud_revenue])
categories = ['AI', 'Cybersecurity', 'Blockchain', 'Cloud']
bar_width = 0.5
x_pos = np.arange(len(years))

fig, ax = plt.subplots(figsize=(14, 8))

# Colors for positive and negative side
positive_color = '#0072B2'
negative_color = '#D55E00'

# Calculate cumulative sum for stack positioning
positive_cum_values = np.cumsum(data, axis=0)
negative_cum_values = np.cumsum(-data[::-1], axis=0)

# Plot each category rectifying the positions based on cumulative values
for i, category in enumerate(categories):
    if i < len(categories) // 2:
        ax.bar(x_pos, data[i], bar_width, label=category, color=positive_color, bottom=positive_cum_values[i-1] if i > 0 else None)
    else:
        ax.bar(x_pos, -data[i], bar_width, label=category, color=negative_color, bottom=negative_cum_values[i-len(categories)//2-1] if i > len(categories)//2 else None)

ax.set_xticks(x_pos)
ax.set_xticklabels(years)

# Display legend
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()