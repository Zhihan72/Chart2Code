import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2030)
main_disciplines = ['Biology', 'Computer Science', 'Physics', 'Mathematics', 'Chemistry']
subcategories = {
    'Biology': ['Molecular Biology', 'Ecology', 'Genetics'],
    'Computer Science': ['AI', 'Cybersecurity', 'Data Science'],
    'Physics': ['Quantum Physics', 'Astrophysics', 'Thermodynamics'],
    'Mathematics': ['Algebra', 'Calculus', 'Statistics'],
    'Chemistry': ['Organic Chemistry', 'Inorganic Chemistry', 'Physical Chemistry']
}

paper_submissions = {discipline: np.array([
    np.arange(50 + i * 10, 50 + i * 10 + len(years) * 10, 10) for i in range(len(subcats))
]) for discipline, subcats in subcategories.items()}

colormaps = ['YlGn', 'BuPu', 'PuRd', 'RdPu', 'Oranges']

fig, axes = plt.subplots(len(main_disciplines), 1, figsize=(14, 12), sharex=True)

for idx, (discipline, subcats) in enumerate(subcategories.items()):
    ax = axes[idx]
    heat_map = ax.imshow(paper_submissions[discipline], cmap=colormaps[idx % len(colormaps)], aspect='auto', interpolation='nearest')
    ax.set_yticks(np.arange(len(subcats)))
    # Color bar and legend removal
    ax.set_yticklabels([])

plt.xticks(ticks=np.arange(len(years)), labels=[''] * len(years))
plt.xlabel('')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()