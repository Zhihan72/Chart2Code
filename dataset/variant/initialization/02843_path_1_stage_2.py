import matplotlib.pyplot as plt
import numpy as np

# Main disciplines and subcategories
years = np.arange(2010, 2030)
main_disciplines = ['Biology', 'Computer Science', 'Physics', 'Mathematics']
subcategories = {
    'Biology': ['Molecular Biology', 'Ecology', 'Genetics'],
    'Computer Science': ['AI', 'Cybersecurity', 'Data Science'],
    'Physics': ['Quantum Physics', 'Astrophysics', 'Thermodynamics'],
    'Mathematics': ['Algebra', 'Calculus', 'Statistics']
}

# Artificial data for paper submissions
paper_submissions = {discipline: np.array([
    np.arange(50 + i * 10, 50 + i * 10 + len(years) * 10, 10) for i in range(len(subcats))
]) for discipline, subcats in subcategories.items()}

# Different color maps for each discipline to shuffle colors
cmap_list = ['viridis', 'plasma', 'inferno', 'magma']

fig, axes = plt.subplots(len(main_disciplines), 1, figsize=(14, 12), sharex=True)

for idx, (discipline, subcats) in enumerate(subcategories.items()):
    ax = axes[idx]
    heat_map = ax.imshow(paper_submissions[discipline], cmap=cmap_list[idx], aspect='auto', interpolation='nearest')
    ax.set_title(f'{discipline} Trends in Paper Submissions', fontsize=14, fontweight='bold')
    
    ax.set_yticks(np.arange(len(subcats)))
    ax.set_yticklabels(subcats, fontsize=10)
    
    for i, subcat in enumerate(subcats):
        growth_rate = np.round(((paper_submissions[discipline][i, -1] - paper_submissions[discipline][i, 0]) / paper_submissions[discipline][i, 0]) * 100, 2)
        ax.text(len(years)-1, i, f'Growth: {growth_rate}%', fontsize=9, color='black', ha='left', va='center', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
    
    cbar = fig.colorbar(heat_map, ax=ax, orientation='vertical')
    cbar.set_label('Submissions', fontsize=10)

plt.suptitle('Reduced Trends in Scientific Paper Submissions (2010-2029)', fontsize=16, fontweight='bold', y=0.95)
plt.xticks(ticks=np.arange(len(years)), labels=years, rotation=45, ha='right')
plt.xlabel('Year', fontsize=12)
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()