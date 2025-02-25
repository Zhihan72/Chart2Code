import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)

# Revenue data (in billions USD) with manually altered contents
ai_revenue = [12, 6, 40, 9, 25, 18]           # Random permutation of original AI revenue
cybersecurity_revenue = [23, 18, 30, 45, 15, 20] # Random permutation of cybersecurity revenue
blockchain_revenue = [3, 12, 9, 6, 1, 2]      # Random permutation of blockchain revenue
cloud_revenue = [50, 30, 5, 8, 22, 15]        # Random permutation of cloud revenue

data = np.array([ai_revenue, cybersecurity_revenue, blockchain_revenue, cloud_revenue])
categories = ['AI', 'Cybersecurity', 'Blockchain', 'Cloud']
bar_width = 0.5
x_pos = np.arange(len(years))

fig, ax = plt.subplots(figsize=(14, 8))

positive_color = '#0072B2'
negative_color = '#D55E00'

positive_cum_values = np.cumsum(data, axis=0)
negative_cum_values = np.cumsum(-data[::-1], axis=0)

for i, category in enumerate(categories):
    if i < len(categories) // 2:
        ax.bar(x_pos, data[i], bar_width, color=positive_color, bottom=positive_cum_values[i-1] if i > 0 else None)
    else:
        ax.bar(x_pos, -data[i], bar_width, color=negative_color, bottom=negative_cum_values[i-len(categories)//2-1] if i > len(categories)//2 else None)

ax.set_xticks(x_pos)
ax.set_xticklabels(years)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()