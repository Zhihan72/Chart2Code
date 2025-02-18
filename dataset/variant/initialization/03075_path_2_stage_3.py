import matplotlib.pyplot as plt
import numpy as np

distribution = np.array([30, 20, 15, 25, 10])
# New color set replacing the original colors
colors = ['#FF5733', '#33FFEC', '#DAF7A6', '#FFC300', '#900C3F']
explode = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(distribution, startangle=140, colors=colors, explode=explode, wedgeprops=dict(width=0.3))

plt.show()