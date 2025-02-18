import matplotlib.pyplot as plt
import numpy as np

skills = ['Cultural Awareness', 'Empathy', 'Critical Thinking', 'Creativity', 'Vocabulary']
genres = ['Poetry', 'Fiction', 'Drama', 'Non-Fiction']
data = {
    'Poetry': [8, 7, 9, 5, 6],
    'Fiction': [9, 6, 5, 8, 7],
    'Drama': [5, 6, 9, 8, 7],
    'Non-Fiction': [9, 5, 7, 8, 5],
}

average_skill_scores = np.mean(list(data.values()), axis=0)
average_skill_scores = np.append(average_skill_scores, average_skill_scores[0])

N = len(skills)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

markers = ['o', 's', '^', 'D']  # Different marker types
line_styles = ['-', '--', '-.', ':']  # Different line styles

for i, (genre, values) in enumerate(data.items()):
    values.append(values[0])
    ax.fill(angles, values, label=genre, alpha=0.25)
    ax.plot(angles, values, linestyle=line_styles[i % len(line_styles)], 
            marker=markers[i % len(markers)], linewidth=2)

ax.plot(angles, average_skill_scores, color='black', linestyle=':', linewidth=2, label='Average Competency Level')
ax.scatter(angles[:-1], average_skill_scores[:-1], color='black', zorder=10)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=11)

plt.title("Diving into Literary Competencies:\nGenres Enhancing Diverse Skills", size=16, fontweight='bold', va='bottom', pad=20)
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.2), title='Genres', fontsize=10)

ax.spines['polar'].set_visible(False)  # Remove polar border
ax.grid(linewidth=0.5)  # Make grid lines thinner

plt.tight_layout()
plt.show()