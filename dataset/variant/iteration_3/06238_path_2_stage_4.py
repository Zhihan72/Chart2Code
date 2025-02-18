import matplotlib.pyplot as plt
import numpy as np

# Updated departments and corresponding data points
departments = ['R&D', 'Marketing', 'Sales', 'HR', 'IT', 'Operations', 'Legal', 'Finance']
expenditure = [45, 20, 15, 10, 7, 3, 5, 8]  # in millions
growth_rates = [8, 12, 5, 7, 9, 3, 4, 10]

# Updated color scheme to match the increased dataset
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF69B4', '#FF4500', '#778899']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

wedges, texts, autotexts = ax1.pie(
    expenditure, explode=explode, colors=colors, autopct='%1.1f%%',
    startangle=90, shadow=False, wedgeprops=dict(edgecolor='gray', linestyle='--', linewidth=2.0))

y_pos = np.arange(len(departments))
ax2.barh(y_pos, growth_rates, color=colors, hatch="/", edgecolor='green')

for i, v in enumerate(growth_rates):
    ax2.text(v + 0.5, i, f"{v}%", color='purple', va='center', fontweight='bold')

ax2.grid(True, which='both', linestyle='dotted', linewidth=0.5, color='grey')

for spine in ax2.spines.values():
    spine.set_edgecolor('blue')
    spine.set_linestyle('dashed')

plt.tight_layout()
plt.show()