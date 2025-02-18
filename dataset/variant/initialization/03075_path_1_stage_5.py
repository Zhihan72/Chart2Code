import matplotlib.pyplot as plt
import numpy as np

distribution = np.array([25, 10, 20, 30])
colors = ['#FFD700', '#66B3FF', '#FF9999', '#FFCC99']
explode = (0, 0, 0, 0.1)

fig, ax = plt.subplots(figsize=(8, 8))
# Creating a donut pie chart by setting a wedgeprops parameter to create a hole
wedges, _, autotexts = ax.pie(distribution, autopct='%1.1f%%', startangle=120, colors=colors, 
                              explode=explode, wedgeprops=dict(width=0.3))

plt.setp(autotexts, size=12, weight="normal")

plt.tight_layout()
plt.show()