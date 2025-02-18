import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

# Backstory:
# This scatter plot analyzes the relationship between the stress levels and creative productivity among artists. 
# The chart includes fictional data depicting how varying stress levels might correlate with the number of new artworks produced over a month.

# Constructing contextual data inputs
stress_levels = np.array([2, 3, 5, 7, 8, 6, 4, 9, 1, 4.5])
artworks_produced = np.array([12, 15, 20, 24, 22, 19, 17, 26, 10, 14])

# Calculate correlation
corr_coefficient, _ = pearsonr(stress_levels, artworks_produced)
corr_text = f"Pearson Correlation: {corr_coefficient:.2f}"

# Figure setup
plt.figure(figsize=(12, 8))

# Scatter plot
scatter = plt.scatter(stress_levels, artworks_produced, color='purple', s=150, alpha=0.6, edgecolor='black')

# Title and labels
plt.title("Impact of Stress Levels on Creative Productivity\nA Study Among Fictional Artists", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Stress Levels (1-10 scale)", fontsize=14)
plt.ylabel("Artworks Produced in a Month", fontsize=14)

# Annotate points
for i, txt in enumerate(range(1, 11)):
    plt.annotate(f"Artist {txt}", (stress_levels[i], artworks_produced[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

# Adding the correlation text on plot
plt.text(6, 15, corr_text, fontsize=12, color='blue', bbox=dict(facecolor='white', edgecolor='blue', pad=5.0))

# Customize the grid
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()