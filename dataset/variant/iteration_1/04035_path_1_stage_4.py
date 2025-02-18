import matplotlib.pyplot as plt
import numpy as np

activities = ['Social Media', 'Gaming', 'Studying', 'Entertainment', 'Miscellaneous']
hours_spent = [3, 2, 4, 2, 3]

fig, ax1 = plt.subplots(figsize=(12, 5))

bars1 = ax1.bar(activities, hours_spent, color='darkcyan', alpha=0.8)
ax1.set_ylim(0, 5)

plt.tight_layout()
plt.show()