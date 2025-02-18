import matplotlib.pyplot as plt
import numpy as np

distribution = np.array([30, 20, 15, 25, 10])
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
explode = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
# Remove labels and text by not using 'labels' and setting 'autopct' to None
ax.pie(distribution, startangle=140, colors=colors, explode=explode, wedgeprops=dict(width=0.3))

plt.show()