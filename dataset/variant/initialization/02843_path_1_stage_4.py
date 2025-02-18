import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2030)
main_disciplines = ['Biology', 'Computer Science', 'Physics', 'Mathematics']
subcategories = {
    'Biology': ['Genetics', 'Ecology', 'Molecular Biology'],
    'Computer Science': ['Cybersecurity', 'AI', 'Data Science'],
    'Physics': ['Astrophysics', 'Thermodynamics', 'Quantum Physics'],
    'Mathematics': ['Calculus', 'Statistics', 'Algebra']
}

paper_submissions = {discipline: np.array([
    np.arange(50 + i * 10, 50 + i * 10 + len(years) * 10, 10) for i in range(len(subcats))
]) for discipline, subcats in subcategories.items()}

cmap_list = ['plasma', 'inferno', 'viridis', 'magma']

fig, axes = plt.subplots(len(main_disciplines), 1, figsize=(14, 12), sharex=True)

for idx, (discipline, subcats) in enumerate(subcategories.items()):
    ax = axes[idx]
    ax.imshow(paper_submissions[discipline], cmap=cmap_list[idx], aspect='auto', interpolation='nearest')
    ax.set_title(f'Submissions in {discipline} Over Years', fontsize=14, fontweight='bold')
    
    ax.set_yticks(np.arange(len(subcats)))
    ax.set_yticklabels(subcats, fontsize=10)
    
    for i, subcat in enumerate(subcats):
        growth_rate = np.round(((paper_submissions[discipline][i, -1] - paper_submissions[discipline][i, 0]) / paper_submissions[discipline][i, 0]) * 100, 2)
        ax.text(len(years)-1, i, f'{subcat}: {growth_rate}% inc', fontsize=9, color='black', ha='left', va='center', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
    
    # Eliminate the colorbar
    # cbar = fig.colorbar(heat_map, ax=ax, orientation='vertical')
    # cbar.set_label('Number of Submissions', fontsize=10)

# Remove spines for all axes
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

plt.suptitle('Shifting Scientific Paper Submissions (2010-2029)', fontsize=16, fontweight='bold', y=0.95)
plt.xticks(ticks=np.arange(len(years)), labels=years, rotation=45, ha='right')
plt.xlabel('Calendar Year', fontsize=12)
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()