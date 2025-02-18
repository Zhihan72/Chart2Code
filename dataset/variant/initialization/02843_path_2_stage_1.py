import matplotlib.pyplot as plt
import numpy as np

# Extended years and expanded disciplines with subcategories
years = np.arange(2010, 2030)
main_disciplines = ['Biology', 'Computer Science', 'Physics', 'Mathematics', 'Chemistry']
subcategories = {
    'Biology': ['Molecular Biology', 'Ecology', 'Genetics'],
    'Computer Science': ['AI', 'Cybersecurity', 'Data Science'],
    'Physics': ['Quantum Physics', 'Astrophysics', 'Thermodynamics'],
    'Mathematics': ['Algebra', 'Calculus', 'Statistics'],
    'Chemistry': ['Organic Chemistry', 'Inorganic Chemistry', 'Physical Chemistry']
}

# Artificial data for paper submissions for each subcategory
paper_submissions = {discipline: np.array([
    np.arange(50 + i * 10, 50 + i * 10 + len(years) * 10, 10) for i in range(len(subcats))
]) for discipline, subcats in subcategories.items()}

# Create a figure with a set of subplots for each main discipline
fig, axes = plt.subplots(len(main_disciplines), 1, figsize=(14, 12), sharex=True)

for idx, (discipline, subcats) in enumerate(subcategories.items()):
    ax = axes[idx]
    heat_map = ax.imshow(paper_submissions[discipline], cmap='YlGnBu', aspect='auto', interpolation='nearest')
    
    # Set yticks without labels
    ax.set_yticks(np.arange(len(subcats)))
    
    # Add color bar without label
    cbar = fig.colorbar(heat_map, ax=ax, orientation='vertical')

# Remove suptitle
plt.suptitle('')

# Remove xticks labels
plt.xticks(ticks=np.arange(len(years)), labels=[''] * len(years))

# Remove xlabel
plt.xlabel('')

# Tight layout adjustment
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Display the plot
plt.show()