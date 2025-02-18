import matplotlib.pyplot as plt
import numpy as np

years = np.arange(3000, 3051, 10)
tech_advancement = {
    'AI and Robotics': np.array([12, 18, 19, 22, 37, 41]),
    'Sustainable Energy': np.array([7, 9, 16, 19, 32, 36]),
    'Biotechnology': np.array([9, 11, 17, 25, 26, 31]),
}

line_colors = ['#FF4500', '#2E8B57', '#6A5ACD']

fig, ax = plt.subplots(figsize=(9, 9))
for (tech, improvements), color in zip(tech_advancement.items(), line_colors):
    ax.plot(years, improvements, marker='o', linewidth=2.5, color=color)

ax.set_title('Technological Advancements (3000-3050)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Advancement Index', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()