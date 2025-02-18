import matplotlib.pyplot as plt
import numpy as np

tea_consumption = [2.5, 4.2, 1.8, 3.6, 2.9]

# Sort the data in descending order
sorted_consumption = sorted(tea_consumption, reverse=True)

fig, ax = plt.subplots(figsize=(10, 6))
x_pos = np.arange(len(sorted_consumption))
colors = ['#B5651D', '#8B4513', '#A0522D', '#CD853F', '#D2691E']

# Create bars using the sorted data
bars = ax.bar(x_pos, sorted_consumption, color=colors, alpha=0.8, width=0.5)

ax.set_xticks([])

plt.tight_layout()
plt.show()