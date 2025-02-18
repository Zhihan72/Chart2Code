import matplotlib.pyplot as plt
import numpy as np

# Skills and genres are shuffled for random labeling
skills = ['Cultural Awareness', 'Empathy', 'Critical Thinking', 'Creativity', 'Vocabulary']
genres = ['Poetry', 'Fiction', 'Drama', 'Non-Fiction']
data = {
    'Poetry': [9, 6, 8, 5, 7],
    'Fiction': [8, 7, 9, 6, 5],
    'Drama': [6, 8, 7, 5, 9],
    'Non-Fiction': [5, 9, 5, 7, 8],
}

average_skill_scores = np.mean(list(data.values()), axis=0)
average_skill_scores = np.append(average_skill_scores, average_skill_scores[0])

N = len(skills)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

for genre in data:
    data[genre].append(data[genre][0])

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

uniform_color = '#4682B4'
for values in data.values():
    ax.fill(angles, values, color=uniform_color, alpha=0.25)
    ax.plot(angles, values, color=uniform_color, linewidth=2)

ax.plot(angles, average_skill_scores, color='black', linestyle='dashed', linewidth=2, label='Average Competency Level')
ax.scatter(angles[:-1], average_skill_scores[:-1], color='black', zorder=10)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=11)

plt.title("Diving into Literary Competencies:\nDifferent Genres Enhancing Diverse Skills", size=16, fontweight='bold', va='bottom', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), title='Genres of Literature', fontsize=10)

plt.tight_layout()
plt.show()