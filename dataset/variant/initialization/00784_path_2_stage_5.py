import numpy as np
import matplotlib.pyplot as plt

attributes = ['Fragrance', 'Sourness', 'Heaviness', 'Sweet', 'Aftertaste']
num_attributes = len(attributes)

morning_brew = [7, 5, 6, 8, 7]
tropical_twist = [8, 7, 5, 9, 6]

data = np.array([morning_brew, tropical_twist])
data = np.concatenate((data, data[:, [0]]), axis=1)

angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

labels = ["Early Delight", "Island Breeze"]
colors = ['#2CA02C', '#FF7F0E']  # Swapped the colors

for i, color in enumerate(colors):
    ax.fill(angles, data[i], color=color, alpha=0.3, label=labels[i])
    ax.plot(angles, data[i], color=color, linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=11, fontstyle='italic')
ax.set_title('Sensory Adventure: Exploring Coffee Flavor Profiles', fontsize=15, pad=30)
ax.legend(loc='upper left', bbox_to_anchor=(0.8, 0.2))
ax.grid(color='gray', linestyle=':', linewidth=0.7)

plt.tight_layout()
plt.show()