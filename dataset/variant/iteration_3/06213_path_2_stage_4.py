import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperature = [5, 7, 12, 18, 22, 25, 27, 26, 22, 16, 10, 6]

fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(months, temperature, color='purple', marker='o', linestyle='-', linewidth=2, markersize=5)

plt.tight_layout()
plt.show()