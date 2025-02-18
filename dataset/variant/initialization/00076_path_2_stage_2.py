import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)

python_popularity = np.array([55, 93, 70, 97, 60, 65, 50, 85, 78, 90])
javascript_popularity = np.array([63, 82, 72, 67, 80, 60, 78, 70, 75, 85])
java_popularity = np.array([75, 66, 65, 78, 64, 80, 72, 67, 68, 70])

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, python_popularity, color='tab:blue', marker='o', linewidth=2.5, linestyle='-')
ax.plot(years, javascript_popularity, color='tab:green', marker='^', linewidth=2.5, linestyle='--')
ax.plot(years, java_popularity, color='tab:red', marker='s', linewidth=2.5, linestyle='-.')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)
ax.set_title('The Evolution of Programming Language Popularity\nin the Digital Age (2010-2019)', fontsize=14)

plt.tight_layout()
plt.show()