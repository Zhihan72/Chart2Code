import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

python_pop = np.array([35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
js_pop = np.array([40, 42, 44, 46, 48, 50, 52, 55, 57, 59, 62])
java_pop = np.array([50, 52, 54, 56, 58, 59, 60, 61, 62, 63, 64])
csharp_pop = np.array([30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, python_pop, label='Python', color='green', marker='x', linestyle='-', linewidth=2.5)
ax.plot(years, js_pop, label='JavaScript', color='purple', marker='o', linestyle='-.', linewidth=1.5)
ax.plot(years, java_pop, label='Java', color='blue', marker='h', linestyle='--', linewidth=2)
ax.plot(years, csharp_pop, label='C#', color='red', marker='v', linestyle=':', linewidth=2)

ax.set_title('Popularity of Programming Languages (2010-2020)', fontsize=18, fontweight='normal')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Popularity Index', fontsize=14)

ax.legend(loc='upper right', fontsize=12)
ax.grid(True, linestyle='-', alpha=0.8)

plt.tight_layout()
plt.show()