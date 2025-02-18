import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
chocolate_types = ['Dark Chocolate', 'Milk Chocolate', 'White Chocolate']

dark_chocolate = [18, 15, 22, 20, 19, 18, 21, 24, 23, 20, 22, 21]
milk_chocolate = [28, 25, 30, 27, 30, 26, 34, 33, 31, 29, 30, 28]
white_chocolate = [12, 14, 13, 10, 12, 15, 16, 18, 17, 16, 14, 15]

colors = ['#C70039', '#FFBF00', '#6A0572']
x = np.arange(len(months))

dark_negative = [-value/2 for value in dark_chocolate]
milk_negative = [-value/2 for value in milk_chocolate]
white_negative = [-value/2 for value in white_chocolate]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

ax1.barh(x, dark_negative, color=colors[0], edgecolor='black')
ax1.barh(x, milk_negative, left=dark_negative, color=colors[1], edgecolor='black')
ax1.barh(x, white_negative, left=[sum(values) for values in zip(dark_negative, milk_negative)], color=colors[2], edgecolor='black')

ax1.barh(x, dark_chocolate, color=colors[0], edgecolor='black')
ax1.barh(x, milk_chocolate, left=dark_chocolate, color=colors[1], edgecolor='black')
ax1.barh(x, white_chocolate, left=[sum(values) for values in zip(dark_chocolate, milk_chocolate)], color=colors[2], edgecolor='black')

ax1.set_yticks(x)
ax1.set_yticklabels(months)
ax1.set_xlabel('Output (K bars)', fontsize=12)
ax1.set_title('Candy Factory: Diversified Month-wise Production!', fontsize=16, fontweight='bold')

# Remove border (spines)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

total_production = np.array(dark_chocolate) + np.array(milk_chocolate) + np.array(white_chocolate)
ax2.plot(months, total_production, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)
ax2.fill_between(months, total_production, color='lightblue', alpha=0.3)

ax2.set_xlabel('Month Span', fontsize=12)
ax2.set_ylabel('Total Output (K bars)', fontsize=12)
ax2.set_title('Total Bars Annually: The Curve', fontsize=16, fontweight='bold')

# Remove border (spines)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()