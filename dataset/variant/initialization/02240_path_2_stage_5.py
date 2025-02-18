import matplotlib.pyplot as plt
import numpy as np

styles = ["Samurai", "Medieval", "Rapier"]
scores_kenjutsu = [85, 88, 82, 89, 90, 95, 83, 87, 88, 92, 94, 78, 85, 81, 89]
scores_longsword = [78, 75, 80, 76, 84, 83, 82, 79, 77, 81, 85, 88, 86, 90]
scores_rapier = [90, 92, 94, 95, 88, 93, 91, 90, 92, 94, 89, 85, 87, 93, 91]

data = [scores_kenjutsu, scores_longsword, scores_rapier]

plt.figure(figsize=(10, 6))

bp = plt.boxplot(data, patch_artist=True, notch=False, vert=False,
                 boxprops=dict(facecolor="skyblue", color="midnightblue"),
                 capprops=dict(color="midnightblue"),
                 whiskerprops=dict(color="goldenrod"),
                 flierprops=dict(markerfacecolor='peru', marker='^'),
                 medianprops=dict(color="firebrick"))

plt.title("Swordsmanship Scores", fontsize=16, pad=20)
plt.xlabel("Score", fontsize=12)
plt.ylabel("Styles", fontsize=12)

plt.yticks(np.arange(1, len(styles) + 1), styles, fontsize=11)

plt.grid(axis='y', linestyle=':', alpha=0.5)

plt.tight_layout()

plt.show()