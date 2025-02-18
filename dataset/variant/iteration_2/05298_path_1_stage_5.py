import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Scores for the two categories
dragonscore = [9, 6, 10, 7, 8, 9]
phoenixscore = [8, 9, 9, 5, 8, 7]

# Number of variables we're plotting
num_vars = len(dragonscore)

# Compute evenly-spaced angles representing each axis in a radar chart
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()

# The radar chart is a closed loop, so we need to "complete the circle" by repeating the first value
dragonscore += dragonscore[:1]
phoenixscore += phoenixscore[:1]
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Draw one radar region per category
ax.fill(angles, dragonscore, 'orange', alpha=0.25)
ax.fill(angles, phoenixscore, 'red', alpha=0.25)

# Remove the axis labels and outer circle
plt.xticks([])
plt.yticks([])
plt.ylim(0, 10)

# Display the radar chart
plt.show()