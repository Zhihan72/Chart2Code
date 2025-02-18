import numpy as np
import matplotlib.pyplot as plt

attributes = ['Customer Service', 'Technical Support', 'Pricing', 'Coverage Area', 'Speed']
isp_1 = [6, 8, 5, 7, 9]
isp_2 = [8, 7, 7, 8, 8]
isp_3 = [5, 6, 9, 9, 7]
isp_4 = [9, 8, 8, 5, 6]

data = np.array([isp_1, isp_2, isp_3, isp_4])
num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

data = np.concatenate((data, data[:, [0]]), axis=1)
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff6666']

for i, isp_data in enumerate(data):
    ax.fill(angles, isp_data, color=colors[i], alpha=0.25)
    ax.plot(angles, isp_data, color=colors[i], linewidth=2)

plt.xticks(angles[:-1], attributes, color='black', size=10)
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], [], color="grey", size=10)
plt.ylim(0, 10)

plt.title("Internet Service Providers Comparison", size=16, weight='bold', position=(0.5, 1.05), ha='center')

plt.tight_layout()
plt.show()