import matplotlib.pyplot as plt
import numpy as np

# Altered labels ("Creativity" and "Empathy" switched places; "Critical Thinking" and "Cultural Awareness" switched)
skills = ['Empathy', 'Cultural Awareness', 'Creativity', 'Vocabulary', 'Critical Thinking']

# Altered chart title slightly
plt_title = "Literary Skills Evaluation:\nAbilities by Genre"

# Swapped genre names and their corresponding data
data = {
    'Non-Fiction': [8, 7, 9, 6, 5],
    'Drama': [5, 9, 5, 7, 8],
    'Fiction': [6, 8, 7, 5, 9],
}

average_skill_scores = np.mean(list(data.values()), axis=0)
average_skill_scores = np.append(average_skill_scores, average_skill_scores[0])

N = len(skills)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

for genre in data:
    data[genre].append(data[genre][0])

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

colors = ['#32CD32', '#FFD700', '#4682B4']
markers = ['o', '^', 'D']
linestyles = ['-', '--', ':']

for i, (genre, values) in enumerate(data.items()):
    ax.fill(angles, values, color=colors[i], alpha=0.3)
    ax.plot(angles, values, color=colors[i], linewidth=1.5, linestyle=linestyles[i], label=genre)
    ax.scatter(angles, values, color=colors[i], marker=markers[i], zorder=10)

ax.fill(angles, average_skill_scores, color='gray', alpha=0.2, label='Average Skill Score')
ax.plot(angles, average_skill_scores, color='black', linestyle='-', linewidth=1)
ax.scatter(angles[:-1], average_skill_scores[:-1], color='black', marker='x', zorder=10)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12, fontweight='medium')  # Altered skill labels are displayed here
ax.tick_params(axis='x', which='major', pad=15)

# Modified title based on reshuffled and altered elements
plt.title(plt_title, size=18, fontweight='bold', va='bottom', pad=25)
plt.legend(loc='upper left', bbox_to_anchor=(1.1, 1.05), title='Genres', fontsize=9, frameon=False)

plt.tight_layout()
plt.show()