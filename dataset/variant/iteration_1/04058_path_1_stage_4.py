import numpy as np
import matplotlib.pyplot as plt

decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
coal = [300, 400, 500, 600, 550, 400, 300]
oil = [200, 250, 300, 350, 400, 350, 200]
nuclear = [0, 50, 100, 150, 200, 250, 300]
renewables = [10, 20, 50, 100, 200, 400, 600]

fig, ax = plt.subplots(figsize=(14, 7))

color = 'teal'
ax.plot(decades, coal, color=color, marker='o', linestyle='-', linewidth=2)
ax.plot(decades, oil, color=color, marker='s', linestyle='--', linewidth=2)
ax.plot(decades, nuclear, color=color, marker='D', linestyle=':', linewidth=2)
ax.plot(decades, renewables, color=color, marker='*', linestyle='-', linewidth=2)

plt.xticks(rotation=45)
plt.yticks(np.arange(0, 701, 100))
plt.show()