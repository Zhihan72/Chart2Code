import matplotlib.pyplot as plt

happiness_scores_africa = [4.3, 4.5, 4.7, 4.6, 4.8, 4.4, 4.9, 4.6, 4.7, 4.5, 4.6]
happiness_scores_asia = [5.1, 5.2, 5.0, 5.4, 5.3, 5.2, 5.1, 5.3, 5.4, 5.0, 5.5]
happiness_scores_europe = [6.7, 6.8, 6.9, 6.8, 6.7, 6.9, 7.0, 6.8, 6.9, 6.7, 7.1]
happiness_scores_north_america = [6.1, 6.3, 6.2, 6.5, 6.4, 6.5, 6.2, 6.6, 6.7, 6.8, 6.4]
happiness_scores_south_america = [5.8, 5.7, 5.9, 5.8, 5.9, 6.0, 5.6, 6.1, 5.9, 5.8, 6.0]
happiness_scores_oceania = [7.2, 7.0, 7.1, 7.3, 7.4, 7.1, 7.5, 7.2, 7.3, 7.2, 7.4]

data = [
    happiness_scores_africa,
    happiness_scores_asia,
    happiness_scores_europe,
    happiness_scores_north_america,
    happiness_scores_south_america,
    happiness_scores_oceania
]

labels = ['Afr', 'Asi', 'Eur', 'N. Am', 'S. Am', 'Oce']

fig, ax = plt.subplots(figsize=(10, 6))

boxplot = ax.boxplot(
    data, 
    patch_artist=True, 
    notch=True, 
    vert=False,  # Change to horizontal boxplot
    boxprops=dict(facecolor='lightblue', color='blue'),
    whiskerprops=dict(color='gray', linestyle='--'),
    capprops=dict(color='black', linewidth=1.5),
    medianprops=dict(color='darkorange', linewidth=2),
    flierprops=dict(marker='o', color='red', markersize=5, alpha=0.5)
)

ax.set_title("Happiness Index (2010-2020)", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Score", fontsize=12)  # Changed from 'Continent' to 'Score'
ax.set_ylabel("Continent", fontsize=12)  # Changed from 'Score' to 'Continent'
ax.set_yticklabels(labels, fontsize=11, rotation=0)  # Adjusted labels for horizontal orientation

ax.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()