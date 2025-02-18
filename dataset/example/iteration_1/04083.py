import matplotlib.pyplot as plt
import numpy as np

# Title and Backstory:
# "The Battle of Ancient Civilizations: Technological Advancements and Population Growth"
# This chart will draw a comparison between technological advancements and population growth in five ancient civilizations from 500 BCE to 500 CE.

# Define the civilizations
civilizations = ['Ancient Egypt', 'Chinese Han', 'Roman Empire', 'Ancient Greece', 'Maurya Empire']

# Define years from 500 BCE to 500 CE (1000 years)
years = np.arange(-500, 501, 100)

# Technological advancement indices (fictional)
tech_advancements = {
    'Ancient Egypt': [15, 17, 20, 25, 27, 30, 32, 34, 35, 37, 40],
    'Chinese Han': [10, 15, 20, 30, 40, 50, 55, 60, 62, 65, 70],
    'Roman Empire': [5, 10, 20, 35, 50, 70, 90, 105, 120, 140, 150],
    'Ancient Greece': [10, 15, 18, 22, 28, 35, 40, 45, 50, 55, 60],
    'Maurya Empire': [8, 12, 18, 25, 30, 40, 45, 48, 50, 52, 55]
}

# Population growth (millions, fictional data)
population_growth = {
    'Ancient Egypt': [1, 1.2, 1.5, 2, 2.5, 3, 3.5, 4, 4.2, 4.4, 4.5],
    'Chinese Han': [2, 2.5, 3, 4, 5, 6, 7, 7.5, 8, 8.2, 8.5],
    'Roman Empire': [1, 1.5, 2, 3, 4.5, 6, 8, 10, 12, 13, 13.5],
    'Ancient Greece': [1, 1.1, 1.3, 1.6, 2, 2.5, 2.8, 3, 3.2, 3.4, 3.5],
    'Maurya Empire': [3, 3.5, 4, 4.5, 5.5, 6.5, 7.2, 8, 8.2, 8.5, 9]
}

# Create the plot
fig, axs = plt.subplots(2, 1, figsize=(14, 10))

# Plot technological advancements
for civ, advancements in tech_advancements.items():
    axs[0].plot(years, advancements, marker='o', label=civ)

# Configure the first subplot (Technological advancements)
axs[0].set_title('Technological Advancements in Ancient Civilizations (500 BCE - 500 CE)', fontsize=14, fontweight='bold')
axs[0].set_ylabel('Tech Advancement Index', fontsize=12)
axs[0].legend(loc='upper left', fontsize=10, frameon=False)
axs[0].grid(True, linestyle='--', alpha=0.7)

# Plot population growth
for civ, population in population_growth.items():
    axs[1].plot(years, population, marker='x', linestyle='dashed', label=civ)

# Configure the second subplot (Population growth)
axs[1].set_title('Population Growth in Ancient Civilizations (500 BCE - 500 CE)', fontsize=14, fontweight='bold')
axs[1].set_ylabel('Population (millions)', fontsize=12)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].legend(loc='upper left', fontsize=10, frameon=False)
axs[1].grid(True, linestyle='--', alpha=0.7)

# Annotate with additional information
annotations = [
    (-400, 35, "Pyramid Building"),
    (0, 70, "Invention of Paper"),
    (100, 150, "Roman Engineering Peak"),
    (200, 60, "Greek Philosophy Flourish"),
    (500, 55, "Maurya Golden Era")
]

for (x, y, text) in annotations:
    axs[0].annotate(text, xy=(x, y), xytext=(x+50, y+10),
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.8),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', color='black'))

# Improve layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()