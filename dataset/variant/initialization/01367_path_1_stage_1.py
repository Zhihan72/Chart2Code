import matplotlib.pyplot as plt
import numpy as np

skills = ['Creativity', 'Critical Thinking', 'Empathy', 'Vocabulary', 'Cultural Awareness']
genres = ['Fiction', 'Non-Fiction', 'Poetry', 'Drama']

data = {
    'Fiction': [8, 7, 9, 6, 5],
    'Non-Fiction': [5, 9, 5, 7, 8],
    'Poetry': [9, 6, 8, 5, 7],
    'Drama': [6, 8, 7, 5, 9],
}

average_skill_scores = np.mean(list(data.values()), axis=0)
average_skill_scores = np.append(average_skill_scores, average_skill_scores[0])

N = len(skills)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

for genre in data:
    data[genre].append(data[genre][0])

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
for i, (genre, values) in enumerate(data.items()):
    ax.fill(angles, values, color=colors[i], alpha=0.25)
    ax.plot(angles, values, color=colors[i], linewidth=2, label=genre)

ax.fill(angles, average_skill_scores, color='gray', alpha=0.1, label='Average Skill Score')
ax.plot(angles, average_skill_scores, color='black', linestyle='dashed', linewidth=2)
ax.scatter(angles[:-1], average_skill_scores[:-1], color='black', zorder=10)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=11)

plt.title("Exploring Literary Skills:\nHow Different Genres Foster Diverse Abilities", size=16, fontweight='bold', va='bottom', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), title='Literary Genres', fontsize=10)

plt.tight_layout()
plt.show()