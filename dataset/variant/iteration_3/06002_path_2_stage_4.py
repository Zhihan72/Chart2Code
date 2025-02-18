import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

# Data inputs (manually shuffled)
stress_levels = np.array([7, 1, 5, 3, 8, 6, 4.5, 9, 2, 4])
artworks_produced = np.array([24, 12, 20, 15, 22, 19, 14, 26, 10, 17])

# Calculate correlation
corr_coefficient, _ = pearsonr(stress_levels, artworks_produced)
corr_text = f"Coefficient of Correlation: {corr_coefficient:.2f}"

plt.figure(figsize=(12, 8))

# Define a set of manually shuffled colors for each data point
colors = ['red', 'green', 'blue', 'orange', 'cyan', 'magenta', 'yellow', 'pink', 'grey', 'purple']

# Scatter plot with shuffled colors
plt.scatter(stress_levels, artworks_produced, color=colors, s=150, alpha=0.6, edgecolor='black')

# Title and labels
plt.title("Creative Outputs & Stress\nAn Imaginary Survey", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Stress Index (1-10)", fontsize=14)
plt.ylabel("Monthly Art Creations", fontsize=14)

# Annotate points
for i, txt in enumerate(range(1, 11)):
    plt.annotate(f"Participant {txt}", (stress_levels[i], artworks_produced[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

# Adding the correlation text on plot
plt.text(6, 15, corr_text, fontsize=12, color='blue', bbox=dict(facecolor='white', edgecolor='blue', pad=5.0))

# Display the plot
plt.show()