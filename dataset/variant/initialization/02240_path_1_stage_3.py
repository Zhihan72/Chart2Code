import matplotlib.pyplot as plt
import numpy as np

styles = ["Samurai\nKenjutsu", "Medieval\nLongsword", "Renaissance\nRapier", "Viking\nSwordsmanship"]
scores_kenjutsu = [85, 88, 82, 89, 90, 95, 83, 87, 88, 92, 94, 78, 85, 81, 89]
scores_longsword = [78, 75, 80, 76, 84, 83, 82, 79, 77, 81, 85, 88, 86, 90]
scores_rapier = [90, 92, 94, 95, 88, 93, 91, 90, 92, 94, 89, 85, 87, 93, 91]
scores_viking = [70, 72, 68, 74, 77, 76, 75, 73, 69, 70, 72, 74, 76, 71, 75]

data = [scores_kenjutsu, scores_longsword, scores_rapier, scores_viking]

plt.figure(figsize=(10, 6))

bp = plt.boxplot(data, patch_artist=True, notch=False, vert=True,
                 boxprops=dict(facecolor="orange", color="black"),
                 capprops=dict(color="green"),
                 whiskerprops=dict(color="red"),
                 flierprops=dict(markerfacecolor='purple', marker='*', markersize=12),
                 medianprops=dict(color="yellow"))

plt.title("Legendary Swordsmanship Festival:\nScores of Various Sword Styles", fontsize=16, pad=20)
plt.xlabel("Swordsmanship Styles", fontsize=12)
plt.ylabel("Score", fontsize=12)

plt.xticks(np.arange(1, len(styles) + 1), styles, fontsize=11)
plt.grid(axis='y', linestyle='-.', alpha=0.7)

plt.tight_layout()
plt.show()