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

for i in range(4):
    wedges, texts, autotexts = ax.flatten()[i].pie(
        energy_data[i],
        autopct='%1.1f%%',
        startangle=140,
        colors=shuffled_colors,
        explode=explode,
        textprops=dict(color="black", fontsize=10)
    )

    # Convert the pie chart to a donut chart by setting the 'width' parameter
    for wedge in wedges:
        wedge.set_edgecolor('w')
        wedge.set_linewidth(1.5)

    # Add a circle at the center of pie to make it a donut
    center_circle = plt.Circle((0,0), 0.70, fc='white')
    ax.flatten()[i].add_artist(center_circle)

    ax.flatten()[i].set_frame_on(False)

ax_eff = fig.add_subplot(224)
ax_eff.bar(range(4), efficiency_ratios, color=shuffled_colors, edgecolor='black', linewidth=1.5)
ax_eff.set_frame_on(False)

plt.show()