import matplotlib.pyplot as plt
import numpy as np

years = np.array(list(range(2015, 2026)))

python_popularity = [20, 25, 30, 35, 42, 48, 55, 60, 66, 70, 75]
javascript_popularity = [30, 28, 27, 25, 23, 22, 20, 19, 18, 17, 15]
java_popularity = [25, 24, 23, 22, 20, 18, 17, 15, 13, 12, 10]
cpp_popularity = [25, 23, 20, 18, 15, 12, 8, 6, 3, 1, 0]

plt.figure(figsize=(12, 6))

# Use a consistent color for all data groups
consistent_color = 'purple'

plt.plot(years, python_popularity, marker='o', linestyle='-', color=consistent_color, linewidth=2, label='Python')
plt.plot(years, javascript_popularity, marker='s', linestyle='--', color=consistent_color, linewidth=2, label='JavaScript')
plt.plot(years, java_popularity, marker='^', linestyle='-.', color=consistent_color, linewidth=2, label='Java')
plt.plot(years, cpp_popularity, marker='x', linestyle=':', color=consistent_color, linewidth=2, label='C++')

# Update annotations to use consistent color
for (x, y) in zip(years, python_popularity):
    plt.text(x, y + 1, f'{y}%', color=consistent_color, fontsize=8, ha='center')

for (x, y) in zip(years, javascript_popularity):
    plt.text(x, y - 2, f'{y}%', color=consistent_color, fontsize=8, ha='center')

for (x, y) in zip(years, java_popularity):
    plt.text(x, y - 2.5, f'{y}%', color=consistent_color, fontsize=8, ha='center')

for (x, y) in zip(years, cpp_popularity):
    plt.text(x, y + 1, f'{y}%', color=consistent_color, fontsize=8, ha='center')

plt.title('Evolution of Programming Languages Popularity\nAmong Students (2015-2025)', fontsize=14, fontweight='bold', ha='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Student Preference (%)', fontsize=12)

plt.xticks(years, rotation=45)
plt.yticks(range(0, 81, 10))

plt.legend(title='Programming Languages', fontsize=10, loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()