import matplotlib.pyplot as plt
import numpy as np

# Randomly selected names for civilizations
civilizations = ['Han Dynasty', 'Greek City-States', 'Roman Empire', 'Egyptian Empire', 'Persian Empire', 'Indus Valley']

# Randomly altered influence scores and population figures
influence = np.array([70, 95, 85, 65, 90, 88]) 
population = np.array([60, 5, 56, 10, 4, 40]) 

fig, ax = plt.subplots(figsize=(10, 6))
y_pos = np.arange(len(civilizations))

# Plot with altered values
ax.barh(y_pos, influence, color='skyblue', edgecolor='w', linewidth=0.5, height=0.5)
ax.set_yticks(y_pos)
ax.set_yticklabels(civilizations)

# Adjusted values for population display
for i, pop in enumerate(population):
    ax.text(influence[i], i, f'{pop}M', va='center', ha='right', color='black', fontsize=10)

# Randomly altered textual elements
ax.set_xlabel('Cultural Impact Score', fontsize=12)
ax.set_title('Legacy of Great Civilizations', fontsize=14)
plt.tight_layout()
plt.show()