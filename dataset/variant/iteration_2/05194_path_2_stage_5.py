import matplotlib.pyplot as plt

energy_data = [
    [50, 10, 20, 20],
    [10, 60, 20, 10],
    [20, 20, 40, 20],
    [20, 10, 20, 50]
]

efficiency_ratios = [0.8, 0.6, 0.9, 0.7]

shuffled_colors = ['#FF8A65', '#FFD54F', '#81C784', '#64B5F6']

fig, ax = plt.subplots(2, 2, figsize=(16,16))
explode = (0.1, 0, 0, 0)

# Rearranging the energy data to different subplot positions
plot_order = [2, 0, 3, 1]

for idx, position in enumerate(plot_order):
    wedges, texts, autotexts = ax.flatten()[idx].pie(
        energy_data[position],
        autopct='%1.1f%%',
        startangle=140,
        colors=shuffled_colors,
        explode=explode,
        textprops=dict(color="black", fontsize=10)
    )

    for wedge in wedges:
        wedge.set_edgecolor('w')
        wedge.set_linewidth(1.5)

    center_circle = plt.Circle((0,0), 0.70, fc='white')
    ax.flatten()[idx].add_artist(center_circle)

    ax.flatten()[idx].set_frame_on(False)

# Switching bar chart position from 224 to 221
ax_eff = fig.add_subplot(221)
ax_eff.bar(range(4), efficiency_ratios, color=shuffled_colors, edgecolor='black', linewidth=1.5)
ax_eff.set_frame_on(False)

plt.show()