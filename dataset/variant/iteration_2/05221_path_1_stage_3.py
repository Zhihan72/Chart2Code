import numpy as np
import matplotlib.pyplot as plt

# Expanded list of software tools
software_tools = ["Tool A", "Tool B", "Tool C", "Tool D", "Tool E", "Tool F", "Tool G"]
# Expanded list of cumulative active users
cumulative_active_users = np.array([1890, 1225, 1200, 1425, 1350, 1300, 1100])

sorted_indices = np.argsort(cumulative_active_users)[::-1]
sorted_tools = [software_tools[i] for i in sorted_indices]
sorted_active_users = cumulative_active_users[sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))

# New set of colors for the bars
new_colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#CD5C5C', '#40E0D0']
ax.bar(sorted_tools, sorted_active_users, color=new_colors)

ax.set_xlabel('Software Tool', fontsize=12)
ax.set_ylabel('Cumulative Active Users (in Thousands)', fontsize=12)
ax.set_title('Cumulative Software Tool Usage (2015-2024)', fontsize=16, fontweight='bold')

for i, v in enumerate(sorted_active_users):
    ax.text(i, v + 20, str(v), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()