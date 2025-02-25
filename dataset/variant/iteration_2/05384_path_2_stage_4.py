import numpy as np
import matplotlib.pyplot as plt

attributes = ['Speed', 'Coverage Nation', 'Client Service', 'Tech Helps', 'Price']

# Existing data of four ISPs plus two additional made-up ISPs
isp_1 = [6, 8, 5, 7, 9]
isp_2 = [8, 7, 7, 8, 8]
isp_3 = [5, 6, 9, 9, 7]
isp_4 = [9, 8, 8, 5, 6]
isp_5 = [7, 6, 6, 7, 8]  # New mocked ISP data
isp_6 = [8, 9, 5, 6, 8]  # New mocked ISP data

data = np.array([isp_1, isp_2, isp_3, isp_4, isp_5, isp_6])
num_vars = len(attributes)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
data = np.concatenate((data, data[:, [0]]), axis=1)
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Updated colors list to accommodate additional ISPs
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#9966ff', '#ff6699']

# Plot each ISP's data including new ISPs
for i, isp_data in enumerate(data):
    ax.fill(angles, isp_data, color=colors[i], alpha=0.5)
    ax.plot(angles, isp_data, color=colors[i], linewidth=2)

plt.xticks(angles[:-1], attributes, color='black', size=10)

ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["Two", "Four", "Six", "Eight", "Ten"], color='black', size=10)
plt.ylim(0, 10)

plt.title("ISP Chart: Review of Different Factors", size=16, weight='bold', position=(0.5, 1.1), ha='center')

plt.show()