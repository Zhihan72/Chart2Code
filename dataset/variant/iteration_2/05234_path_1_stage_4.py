import matplotlib.pyplot as plt
import numpy as np

# Data
hobbies = ['Reading', 'Gaming', 'Exercising', 'Cooking', 'Traveling']
hours_spent = np.array([5, 15, 7, 10, 12])

# Colors for each hobby
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFC300']

# Create Horizontal Bar Chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(hobbies, hours_spent, color=colors)

plt.tight_layout()
plt.show()