import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
beverages = ['Coffee', 'Tea', 'Juice']

coffee_preference = np.array([40, 35, 30, 25, 15])
tea_preference = np.array([20, 25, 30, 35, 40])
juice_preference = np.array([40, 40, 40, 40, 45])

fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.6
bar_positions = np.arange(len(age_groups))

# Calculate the starting positions for each segment to enforce the diverging nature
coffee_start = -coffee_preference / 2
tea_start = np.zeros_like(tea_preference)
juice_start = coffee_preference / 2

# Create diverging bars
bars1 = ax.bar(bar_positions, -coffee_preference, bar_width, bottom=coffee_start, label=beverages[0], color='#8B4513')
bars2 = ax.bar(bar_positions, tea_preference, bar_width, bottom=tea_start, label=beverages[1], color='#CD853F')
bars3 = ax.bar(bar_positions, juice_preference, bar_width, bottom=juice_start, label=beverages[2], color='#FBC02D')

# Annotating each segment with the percentage value
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{abs(height)}%',
                    xy=(bar.get_x() + bar.get_width() / 2, (bar.get_y() + bar.get_y() + height) / 2),
                    xytext=(0, 0), 
                    textcoords='offset points',
                    ha='center', va='center', fontsize=10, color='black')

ax.set_title('Beverage Preference Among Different Age Groups', fontsize=16, fontweight='bold')
ax.set_xlabel('Age Groups', fontsize=14)
ax.set_ylabel('Percentage Preference', fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(age_groups)

ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='best', title='Beverage Type', fontsize=12)
plt.axhline(y=0, color='black', linewidth=0.8)  # Central axis for diverging bars

plt.tight_layout()
plt.show()