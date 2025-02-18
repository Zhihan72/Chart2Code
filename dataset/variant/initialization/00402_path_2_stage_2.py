import matplotlib.pyplot as plt

energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal']
percentages = [35, 25, 18, 12, 10]
colors = ['#FFBB33', '#66BB6A', '#42A5F5', '#AB47BC', '#FF7043']

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=[0.1 if energy == 'Solar' else 0 for energy in energy_sources],
)

ax.axis('equal')

plt.show()