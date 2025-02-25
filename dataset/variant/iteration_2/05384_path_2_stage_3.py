import numpy as np
import matplotlib.pyplot as plt

# Randomly altered attribute names
attributes = ['Speed', 'Coverage Nation', 'Client Service', 'Tech Helps', 'Price']

# Unchanged data of four ISPs
isp_1 = [6, 8, 5, 7, 9]
isp_2 = [8, 7, 7, 8, 8]
isp_3 = [5, 6, 9, 9, 7]
isp_4 = [9, 8, 8, 5, 6]

data = np.array([isp_1, isp_2, isp_3, isp_4])
num_vars = len(attributes)

# Preparation for polar plot
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
data = np.concatenate((data, data[:, [0]]), axis=1)
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Plot each ISP's data
for i, isp_data in enumerate(data):
    ax.fill(angles, isp_data, color=colors[i], alpha=0.5)
    ax.plot(angles, isp_data, color=colors[i], linewidth=2)

# Randomly altered group labels
plt.xticks(angles[:-1], attributes, color='black', size=10)

ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["Two", "Four", "Six", "Eight", "Ten"], color='black', size=10)
plt.ylim(0, 10)

# Randomly altered title
plt.title("ISP Chart: Review of Different Factors", size=16, weight='bold', position=(0.5, 1.1), ha='center')

plt.show()