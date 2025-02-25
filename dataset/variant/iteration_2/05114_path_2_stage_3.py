import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Children', 'Teens', 'Adults', 'Seniors', 'Young Adults']
daily_fluid_intake_liters = {
    'Children': [1.0, 1.2, 1.1, 1.4, 1.3, 1.2, 1.1, 1.5, 1.2, 1.3, 1.4],
    'Teens': [1.8, 2.0, 1.9, 2.1, 2.2, 2.1, 2.3, 1.9, 2.0, 2.1, 2.2],
    'Adults': [2.5, 2.8, 2.7, 2.9, 3.0, 3.1, 3.0, 3.2, 2.8, 3.1, 3.0],
    'Seniors': [1.8, 1.9, 1.7, 1.6, 1.8, 1.7, 1.9, 1.8, 1.6, 1.7, 1.8],
    'Young Adults': [2.2, 2.4, 2.5, 2.3, 2.6, 2.4, 2.5, 2.7, 2.5, 2.6, 2.4]
}
hydration_levels = {
    'Children': [70, 75, 73, 80, 78, 75, 73, 82, 76, 79, 81],
    'Teens': [65, 68, 67, 70, 72, 71, 74, 66, 68, 70, 72],
    'Adults': [80, 83, 82, 85, 87, 88, 86, 90, 84, 87, 88],
    'Seniors': [65, 68, 67, 66, 65, 67, 70, 68, 66, 67, 69],
    'Young Adults': [75, 77, 76, 78, 79, 77, 78, 80, 76, 79, 78]
}

colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:orange', 'tab:purple']
markers = ['o', 'v', '^', 's', 'd']
line_styles = ['-', '--', '-.', ':', '-']

fig, ax = plt.subplots(figsize=(12, 8))

for age_group, color, marker, line_style in zip(age_groups, colors, markers, line_styles):
    fluid_intake = daily_fluid_intake_liters[age_group]
    hydration = hydration_levels[age_group]
    ax.scatter(fluid_intake, hydration, color=color, alpha=0.6, edgecolors='black', linewidth=0.5,
               s=100, marker=marker, label=age_group)

plt.title("Drink Up: Hydration vs Fluid Intake", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Daily Fluid Intake (Liters)", fontsize=14)
plt.ylabel("Hydration Levels (%)", fontsize=14)

plt.xticks(np.arange(1.0, 3.5, 0.5))
plt.yticks(np.arange(60, 100, 5))

plt.grid(True, linestyle=line_styles[0], alpha=0.4)

plt.legend(title="Age Groups", fontsize=10, title_fontsize='11')

plt.annotate('High hydration in Adults', xy=(3.1, 88), xytext=(2.6, 85),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='blue')

plt.tight_layout()

plt.show()