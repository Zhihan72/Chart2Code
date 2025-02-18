import matplotlib.pyplot as plt
import numpy as np

# Modified tea_consumption data with one group removed
tea_consumption = [4.2, 1.8, 3.6, 2.9]
sorted_consumption = sorted(tea_consumption, reverse=True)

fig, ax = plt.subplots(figsize=(10, 6))
x_pos = np.arange(len(sorted_consumption))
# Modified colors list corresponding to the reduced data
new_colors = ['#4682B4', '#FFD700', '#C71585', '#32CD32']

bars = ax.bar(x_pos, sorted_consumption, color=new_colors, alpha=0.8, width=0.5)

ax.set_xticks([])

plt.tight_layout()
plt.show()