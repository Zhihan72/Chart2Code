import numpy as np
import matplotlib.pyplot as plt

departments = ["Development", "Marketing", "Sales", "HR", "Customer Support", "R&D"]
quarters = ["Q1", "Q2", "Q3", "Q4"]

productivity_data = np.array([
    [85, 88, 90, 87],  # Development
    [70, 75, 80, 78],  # Marketing
    [90, 92, 89, 88],  # Sales
    [65, 70, 68, 72],  # HR
    [88, 85, 87, 90],  # Customer Support
    [95, 97, 98, 96]   # R&D
])

fig, ax = plt.subplots(figsize=(14, 8))
x = np.arange(len(quarters))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Plot stacked bars
bottom = np.zeros(len(quarters))
for i in range(len(departments)):
    ax.bar(x, productivity_data[i], label=departments[i], color=colors[i], bottom=bottom)
    bottom += productivity_data[i]

ax.set_title("Quarterly Productivity Levels of Tech Company Departments (2023)", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Quarters', fontsize=12)
ax.set_ylabel('Productivity (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(quarters)
ax.set_ylim(0, np.sum(productivity_data, axis=0).max() + 10)

ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Departments", fontsize=10)

ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()