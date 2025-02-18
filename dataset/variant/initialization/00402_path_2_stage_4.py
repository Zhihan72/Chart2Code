import matplotlib.pyplot as plt

energy_sources = ['Geothermal', 'Biomass', 'Hydropower', 'Solar', 'Wind', 'Nuclear', 'Wave']
percentages = [8, 10, 15, 30, 20, 12, 5]
colors = ['#FF7043', '#AB47BC', '#42A5F5', '#FFBB33', '#66BB6A', '#29B6F6', '#78909C']

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=120,
    colors=colors,
    explode=[0.1 if energy == 'Wind' else 0 for energy in energy_sources],
)

ax.axis('equal')

plt.title("Distribution of Renewable Energy Sources")
plt.show()