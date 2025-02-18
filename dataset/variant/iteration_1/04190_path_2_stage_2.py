import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

python_pop = np.array([35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
js_pop = np.array([40, 42, 44, 46, 48, 50, 52, 55, 57, 59, 62])
java_pop = np.array([50, 52, 54, 56, 58, 59, 60, 61, 62, 63, 64])
csharp_pop = np.array([30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])
ruby_pop = np.array([20, 22, 24, 26, 28, 30, 32, 34, 35, 36, 38])

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, python_pop, label='Py', color='blue', marker='o', linestyle='-', linewidth=2)
ax.plot(years, js_pop, label='JS', color='green', marker='s', linestyle='--', linewidth=2)
ax.plot(years, java_pop, label='Java', color='red', marker='^', linestyle='-.', linewidth=2)
ax.plot(years, csharp_pop, label='C#', color='purple', marker='D', linestyle=':', linewidth=2)
ax.plot(years, ruby_pop, label='Ruby', color='brown', marker='*', linestyle='-', linewidth=2)

ax.set_title('Language Popularity (2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Years', fontsize=12)
ax.set_ylabel('Pop. Index', fontsize=12)

ax.legend(loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()