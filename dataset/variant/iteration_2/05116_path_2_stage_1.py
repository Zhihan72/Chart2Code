import matplotlib.pyplot as plt
import numpy as np

# Define magical categories
categories = ['Alchemy', 'Spell Casting', 'Potion Brewing', 'Enchanting', 'Summoning']
N = len(categories)

# Magical power ratings for each faction
wizard_factions = {
    'Elemental Guild': [8, 7, 6, 9, 7],
    'Mystic Union': [6, 9, 5, 8, 6],
    'Arcane Brotherhood': [7, 6, 9, 7, 9],
    'Ethereal Domain': [9, 8, 7, 6, 8]
}

# Convert data to numpy array and ensure the radar chart is closed
data = {name: np.array(values + [values[0]]) for name, values in wizard_factions.items()}

# Compute the angles for radar chart
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# Define colors for each faction
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each faction's magical abilities
for (name, values), color in zip(data.items(), colors):
    ax.fill(angles, values, color=color, alpha=0.25)
    ax.plot(angles, values, color=color, linewidth=2)

# Customize the radar chart
ax.set_xticks(angles[:-1])
ax.set_xticklabels([])  # Remove category labels
ax.set_yticklabels([])  # Remove radial labels
ax.set_ylim(0, 10)

# Remove legend
# Adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()