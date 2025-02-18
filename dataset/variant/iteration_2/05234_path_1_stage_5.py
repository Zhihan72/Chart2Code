import matplotlib.pyplot as plt
import numpy as np

# Data with the "Gaming" group removed
hobbies = ['Reading', 'Exercising', 'Cooking', 'Traveling']
hours_spent = np.array([5, 7, 10, 12])

# Colors for each hobby, excluding the color for removed "Gaming"
colors = ['#FF5733', '#3357FF', '#FF33A6', '#FFC300']

# Create Horizontal Bar Chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(hobbies, hours_spent, color=colors)

plt.tight_layout()
plt.show()