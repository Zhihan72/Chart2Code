import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
python_popularity = np.array([50, 55, 60, 65, 70, 78, 85, 90, 93, 97])
javascript_popularity = np.array([60, 63, 67, 70, 72, 75, 78, 80, 82, 85])
java_popularity = np.array([80, 78, 75, 72, 70, 68, 67, 66, 65, 64])

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, python_popularity, label='Py', color='tab:blue', marker='o', linewidth=2.5, linestyle='-')
ax.plot(years, javascript_popularity, label='JS', color='tab:green', marker='^', linewidth=2.5, linestyle='--')
ax.plot(years, java_popularity, label='Java', color='tab:red', marker='s', linewidth=2.5, linestyle='-.')

ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Popularity', fontsize=12)
ax.set_title('Prog Lang Popularity (2010-2019)', fontsize=14)

ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='lower left', fontsize=10)
plt.tight_layout()
plt.show()