import matplotlib.pyplot as plt
import numpy as np

# Define the swordsmanship styles and their respective scores from competitions
styles = ["Samurai\nKenjutsu", "Medieval\nLongsword", "Renaissance\nRapier", "Viking\nSwordsmanship"]
scores_kenjutsu = [85, 88, 82, 89, 90, 95, 83, 87, 88, 92, 94, 78, 85, 81, 89]
scores_longsword = [78, 75, 80, 76, 84, 83, 82, 79, 77, 81, 85, 88, 86, 90]
scores_rapier = [90, 92, 94, 95, 88, 93, 91, 90, 92, 94, 89, 85, 87, 93, 91]
scores_viking = [70, 72, 68, 74, 77, 76, 75, 73, 69, 70, 72, 74, 76, 71, 75]

# Combine the scores into a list for boxplot
data = [scores_kenjutsu, scores_longsword, scores_rapier, scores_viking]

plt.figure(figsize=(10, 6))

# Create a horizontal box plot
bp = plt.boxplot(data, patch_artist=True, notch=True, vert=False,
                 boxprops=dict(facecolor="lightblue", color="blue"),
                 capprops=dict(color="blue"),
                 whiskerprops=dict(color="blue"),
                 flierprops=dict(markerfacecolor='red', marker='o'),
                 medianprops=dict(color="green"))

plt.title("Legendary Swordsmanship Festival:\nScores of Various Sword Styles", fontsize=16, pad=20)
plt.ylabel("Swordsmanship Styles", fontsize=12)
plt.xlabel("Score", fontsize=12)

# Ensure the y-ticks correspond to the swordsmanship styles
plt.yticks(np.arange(1, len(styles) + 1), styles, fontsize=11)

# Add a vertical grid to improve readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()