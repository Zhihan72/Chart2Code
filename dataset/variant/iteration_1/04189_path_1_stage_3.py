import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
ai_assistants = [120, 150, 130, 100, 60, 30]
smart_homes = [80, 140, 120, 110, 70, 40]

fig, ax = plt.subplots(figsize=(12, 8))

# Bar heights (for horizontal bars)
height = 0.3

# Set the positions of the bars on the y-axis
bar1 = np.arange(len(age_groups))
bar2 = [x + height for x in bar1]

# Plotting horizontal bars
bar_color = 'skyblue'
ax.barh(bar1, ai_assistants, height, label='AI Assistants', color=bar_color, edgecolor='black')
ax.barh(bar2, smart_homes, height, label='Smart Homes', color=bar_color, edgecolor='black')

# Labels and title
ax.set_ylabel('Age Groups', fontsize=12, weight='bold')
ax.set_xlabel('Number of Adopters', fontsize=12, weight='bold')
ax.set_title('Tech Adoption in Different Age Groups for 2023', fontsize=14, weight='bold', pad=20)

# Customize y-axis values
ax.set_yticks([r + height/2 for r in range(len(age_groups))])
ax.set_yticklabels(age_groups, fontsize=12)

# Add value labels next to bars
def add_value_labels(bars, values):
    for bar, value in zip(bars, values):
        ax.text(value + 3, bar, str(value), va='center', color='black', fontsize=10)

add_value_labels(ai_assistants, bar1)
add_value_labels(smart_homes, bar2)

# Adding legend
ax.legend(title='Technologies', loc='upper right', fontsize=10)

# Gridlines for x-axis
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()