import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

python_interest = [12, 17, 21, 28, 39, 51, 63, 72, 74, 78, 86]
java_interest = [42, 37, 34, 31, 27, 26, 24, 21, 23, 19, 20]
javascript_interest = [18, 24, 26, 29, 34, 39, 46, 47, 51, 52, 55]
csharp_interest = [16, 15, 20, 18, 14, 15, 11, 13, 13, 14, 11]
ruby_interest = [14, 14, 12, 9, 8, 9, 8, 5, 6, 7, 4]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, python_interest, marker='o', linestyle='-', color='blue', linewidth=2, label='Python')
ax.plot(years, java_interest, marker='s', linestyle='-', color='green', linewidth=2, label='Java')
ax.plot(years, javascript_interest, marker='^', linestyle='-', color='orange', linewidth=2, label='JS')
ax.plot(years, csharp_interest, marker='d', linestyle='-', color='purple', linewidth=2, label='C#')
ax.plot(years, ruby_interest, marker='x', linestyle='-', color='red', linewidth=2, label='Ruby')

ax.set_title('Search Interest: 2010-2020', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Interest (%)', fontsize=14)

ax.legend(loc='upper left', fontsize=12, title='Langs', title_fontsize=14)

ax.grid(True, linestyle='--', alpha=0.7)

ax.annotate('Python tops', xy=(2018, 72), xytext=(2015, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=12, color='blue')
ax.annotate('JS grows', xy=(2010, 18), xytext=(2014, 30),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=12, color='orange')

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()