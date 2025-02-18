import numpy as np
import matplotlib.pyplot as plt

# Attributes are preserved since they identify the axes
attributes = ['Fragrance', 'Sourness', 'Heaviness', 'Sweet', 'Aftertaste']
num_attributes = len(attributes)

# Data values for each group
morning_brew = [7, 5, 6, 8, 7]
tropical_twist = [8, 7, 5, 9, 6]

# Combined data for radar plot
data = np.array([morning_brew, tropical_twist])
data = np.concatenate((data, data[:, [0]]), axis=1)

# Angles for each attribute
angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

# Create a polar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Randomly altered group labels
labels = ["Early Delight", "Island Breeze"]
colors = ['#FF7F0E', '#2CA02C']

for i, color in enumerate(colors):
    ax.fill(angles, data[i], color=color, alpha=0.3, label=labels[i])
    ax.plot(angles, data[i], color=color, linewidth=2)

# Updated axis labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=11, fontstyle='italic')

# Randomly changed chart title
ax.set_title('Sensory Adventure: Exploring Coffee Flavor Profiles', fontsize=15, pad=30)

# Legend settings
ax.legend(loc='upper left', bbox_to_anchor=(0.8, 0.2))

# Grid styling
ax.grid(color='gray', linestyle=':', linewidth=0.7)

# Adjust layout
plt.tight_layout()
plt.show()