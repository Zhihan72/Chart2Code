import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

python_interest = [10, 15, 20, 30, 40, 50, 60, 70, 75, 80, 85]
java_interest = [40, 38, 35, 33, 30, 28, 25, 23, 22, 20, 18]
javascript_interest = [20, 22, 25, 30, 35, 40, 45, 48, 50, 53, 55]
csharp_interest = [15, 17, 19, 17, 15, 14, 12, 11, 12, 13, 12]
ruby_interest = [15, 13, 11, 10, 9, 8, 7, 6, 6, 6, 5]

php_interest = [25, 28, 30, 28, 25, 23, 20, 18, 17, 16, 15]
swift_interest = [5, 7, 10, 12, 15, 20, 23, 27, 30, 32, 35]

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, python_interest, marker='p', linestyle='--', color='blue', linewidth=2.5)
ax.plot(years, java_interest, marker='*', linestyle=':', color='blue', linewidth=2)
ax.plot(years, javascript_interest, marker='o', linestyle='-', color='blue', linewidth=2.5)
ax.plot(years, csharp_interest, marker='s', linestyle='-.', color='blue', linewidth=2)
ax.plot(years, ruby_interest, marker='d', linestyle='-', color='blue', linewidth=1.5)
ax.plot(years, php_interest, marker='v', linestyle='--', color='blue', linewidth=2)
ax.plot(years, swift_interest, marker='h', linestyle='-', color='blue', linewidth=2)

ax.grid(color='gray', linestyle=':', linewidth=0.5, alpha=0.6)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xticks(years, rotation=45)
plt.legend(['Python', 'Java', 'JavaScript', 'C#', 'Ruby', 'PHP', 'Swift'], loc='lower right', frameon=False)

plt.tight_layout()
plt.show()