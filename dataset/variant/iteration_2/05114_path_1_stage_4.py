import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Youngsters', 'Adolescents', 'Grown-ups', 'Old Folks', 'Youths', 'Sages']
daily_fluid_intake_liters = {
    'Youngsters': [1.0, 1.2, 1.1, 1.4, 1.3, 1.2, 1.1, 1.5, 1.2, 1.3, 1.4],
    'Adolescents': [1.8, 2.0, 1.9, 2.1, 2.2, 2.1, 2.3, 1.9, 2.0, 2.1, 2.2],
    'Grown-ups': [2.5, 2.8, 2.7, 2.9, 3.0, 3.1, 3.0, 3.2, 2.8, 3.1, 3.0],
    'Old Folks': [1.8, 1.9, 1.7, 1.6, 1.8, 1.7, 1.9, 1.8, 1.6, 1.7, 1.8],
    'Youths': [2.6, 2.9, 2.5, 2.7, 2.8, 2.9, 3.0, 3.1, 2.9, 3.3, 3.2],
    'Sages': [1.7, 1.8, 1.5, 1.6, 1.5, 1.6, 1.7, 1.5, 1.6, 1.5, 1.6]
}
hydration_levels = {
    'Youngsters': [70, 75, 73, 80, 78, 75, 73, 82, 76, 79, 81],
    'Adolescents': [65, 68, 67, 70, 72, 71, 74, 66, 68, 70, 72],
    'Grown-ups': [80, 83, 82, 85, 87, 88, 86, 90, 84, 87, 88],
    'Old Folks': [65, 68, 67, 66, 65, 67, 70, 68, 66, 67, 69],
    'Youths': [75, 77, 76, 78, 79, 80, 82, 85, 81, 87, 86],
    'Sages': [60, 63, 62, 65, 64, 63, 66, 64, 63, 62, 64]
}

# Manually shuffled colors
colors = ['tab:red', 'tab:green', 'tab:purple', 'tab:blue', 'tab:brown', 'tab:orange']

fig, ax = plt.subplots(figsize=(12, 8))

for age_group, color in zip(age_groups, colors):
    fluid_intake = daily_fluid_intake_liters[age_group]
    hydration = hydration_levels[age_group]
    ax.scatter(fluid_intake, hydration, color=color, alpha=0.7, edgecolors='black', linewidth=0.5, s=100)

plt.title("Stay Hydrated: Fluid Intake vs Hydration Level\nAcross Age Categories", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Fluid Intake per Day (Liters)", fontsize=14)
plt.ylabel("Hydration Level (%)", fontsize=14)

plt.xticks(np.arange(1.0, 3.5, 0.5))
plt.yticks(np.arange(60, 100, 5))

plt.tight_layout()
plt.show()