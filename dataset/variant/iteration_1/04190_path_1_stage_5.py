import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

python_popularity = np.array([35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
javascript_popularity = np.array([40, 42, 44, 46, 48, 50, 52, 55, 57, 59, 62])
java_popularity = np.array([50, 52, 54, 56, 58, 59, 60, 61, 62, 63, 64])

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(years, python_popularity, color='#FF5733', marker='o', linestyle='-', linewidth=2)
ax.plot(years, javascript_popularity, color='#33FF57', marker='s', linestyle='--', linewidth=2)
ax.plot(years, java_popularity, color='#3357FF', marker='^', linestyle='-.', linewidth=2)

ax.set_title('Language Trends (2010-20)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity', fontsize=12)

plt.tight_layout()
plt.show()