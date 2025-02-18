import matplotlib.pyplot as plt
import numpy as np

metrics = ['Str', 'End', 'Flex', 'Bal', 'Nutr', 'Mental']
ideal_plan = [8, 8, 8, 8, 8, 8]
current_plan = [6, 7, 5, 9, 6, 7]
future_plan = [7, 6, 7, 8, 8, 6]  # New data series

num_vars = len(metrics)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Close the loop by appending the first data point to the end of each series
ideal_plan += ideal_plan[:1]
current_plan += current_plan[:1]
future_plan += future_plan[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], metrics, color='black', size=12)
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
plt.ylim(0, 10)

ax.plot(angles, ideal_plan, color='orange', linewidth=2, linestyle='dashed')
ax.fill(angles, ideal_plan, color='orange', alpha=0.1)

ax.plot(angles, current_plan, color='teal', linewidth=2, linestyle='solid')
ax.fill(angles, current_plan, color='teal', alpha=0.25)

# Adding the future_plan
ax.plot(angles, future_plan, color='purple', linewidth=2, linestyle='dashdot')
ax.fill(angles, future_plan, color='purple', alpha=0.1)

plt.show()