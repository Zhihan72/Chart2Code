import numpy as np
import matplotlib.pyplot as plt

centuries = ['18th', '20th']
methods = ['Stone', 'Brick', 'Wood', 'Steel']

data = np.array([
    [20, 50, 30, 0],
    [10, 20, 30, 40]
])

method_totals = data.sum(axis=0)
sorted_indices = np.argsort(method_totals)[::-1]
sorted_methods = [methods[i] for i in sorted_indices]
sorted_data = data[:, sorted_indices]

x_pos = np.arange(len(methods))

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#D95F02', '#E7298A', '#7B9F35', '#7570B3']

for i in range(len(centuries)):
    ax.bar(x_pos + i*0.2, sorted_data[i], width=0.2, color=colors, alpha=0.8, label=centuries[i])

ax.set_xlabel('Methods', fontsize=12)
ax.set_ylabel('Prevalence (%)', fontsize=12)
ax.set_title('Methods Across Centuries', fontsize=14)
ax.set_xticks(x_pos + 0.3)
ax.set_xticklabels(sorted_methods, fontsize=10, rotation=25, ha='right')
ax.legend(title='Years', fontsize=9)

plt.tight_layout()
plt.show()