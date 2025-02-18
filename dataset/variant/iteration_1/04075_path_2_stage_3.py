import matplotlib.pyplot as plt
import numpy as np

# Data
classical_var = [1.995, 2.07, 2.94, 2.97, 2.7, 2.548, 2.784, 3.0, 3.0, 2.754]
jazz_var = [3.8, 3.78, 4.62, 4.95, 4.968, 4.214, 4.032, 4.1, 5.136, 4.794]
rock_var = [6.175, 5.94, 7.035, 7.48, 7.452, 6.566, 6.24, 6.8, 7.383, 7.14]
electronic_var = [7.885, 7.56, 8.925, 9.46, 9.396, 8.428, 8.16, 8.4, 9.416, 9.078]
violin_plot_data = [classical_var, jazz_var, rock_var, electronic_var]
labels = ["Clas.", "Jazz", "Rock", "Elect."]

fig, ax = plt.subplots(figsize=(10, 6))
violin_parts = ax.violinplot(violin_plot_data, vert=True, showmeans=False, showmedians=True)

colors = ['lightyellow', 'lightblue', 'lightgreen', 'lightpink']
for pc, color in zip(violin_parts['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

violin_parts['cmedians'].set_color('red')
violin_parts['cmedians'].set_linewidth(2)

ax.set_xticks(np.arange(1, len(labels) + 1))
ax.set_xticklabels(labels, fontsize=12)

plt.show()