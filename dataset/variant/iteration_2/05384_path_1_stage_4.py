import numpy as np
import matplotlib.pyplot as plt

# ISP data for different attributes
isp_1 = [6, 8, 5, 7, 9]
isp_2 = [8, 7, 7, 8, 8]
isp_3 = [5, 6, 9, 9, 7]
isp_4 = [9, 8, 8, 5, 6]

data = np.array([isp_1, isp_2, isp_3, isp_4])
num_vars = len(isp_1)  # Need only length of one ISP as we're not labeling

# Angles for the radar chart, with a repeated angle for closure
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
data = np.concatenate((data, data[:, [0]]), axis=1)
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff6666']

# Plot each ISP's data on the radar chart
for i, isp_data in enumerate(data):
    ax.fill(angles, isp_data, color=colors[i], alpha=0.25)
    ax.plot(angles, isp_data, color=colors[i], linewidth=2)

# Remove all textual elements
plt.xticks([], [])
plt.yticks([], [])
plt.ylim(0, 10)

plt.show()