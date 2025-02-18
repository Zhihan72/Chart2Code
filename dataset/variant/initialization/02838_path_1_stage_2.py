import matplotlib.pyplot as plt

# Data for happiness scores
data = [
    [4.3, 4.5, 4.7, 4.6, 4.8, 4.4, 4.9, 4.6, 4.7, 4.5, 4.6],
    [5.1, 5.2, 5.0, 5.4, 5.3, 5.2, 5.1, 5.3, 5.4, 5.0, 5.5],
    [6.7, 6.8, 6.9, 6.8, 6.7, 6.9, 7.0, 6.8, 6.9, 6.7, 7.1],
    [6.1, 6.3, 6.2, 6.5, 6.4, 6.5, 6.2, 6.6, 6.7, 6.8, 6.4],
    [5.8, 5.7, 5.9, 5.8, 5.9, 6.0, 5.6, 6.1, 5.9, 5.8, 6.0]
]

# Labels for the continents
labels = ['Africa', 'Asia', 'Europe', 'North America', 'South America']

fig, ax = plt.subplots(figsize=(10, 6))

# Boxplot without stylistic elements
ax.boxplot(
    data, 
    patch_artist=False,  # No color patches
    notch=True, 
    vert=True
)

# Title and labels
ax.set_title("Global Happiness Index", fontsize=16)
ax.set_xlabel("Continent", fontsize=12)
ax.set_ylabel("Happiness Index Score", fontsize=12)
ax.set_xticklabels(labels, fontsize=11, rotation=15)

# No grid or tight layout
plt.show()