import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1920, 2030, 10)
# Randomly altered temperature changes while preserving the structure
temp_changes = [0.0, 0.15, 0.2, 0.4, 0.1, 0.6, 0.5, 1.0, 0.8, 0.25, 1.2]

plt.figure(figsize=(14, 8))

# Use the same fixed color scheme
new_line_color = 'b'  # blue line
new_fill_color = 'cyan'  # light cyan fill

plt.plot(decades, temp_changes, marker='o', linestyle='-', color=new_line_color, linewidth=2)
plt.fill_between(decades, temp_changes, color=new_fill_color, alpha=0.2)

plt.xticks(decades, rotation=45)
plt.tight_layout()

plt.show()