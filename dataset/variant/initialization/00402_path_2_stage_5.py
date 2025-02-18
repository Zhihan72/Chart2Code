import matplotlib.pyplot as plt

energy_sources = ['Geothermal', 'Biomass', 'Hydropower', 'Solar', 'Wind', 'Nuclear', 'Wave']
percentages = [8, 10, 15, 30, 20, 12, 5]
single_color = '#42A5F5'

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=120,
    colors=[single_color] * len(energy_sources),
    explode=[0.1 if energy == 'Wind' else 0 for energy in energy_sources],
)

ax.axis('equal')

plt.title("Distribution of Renewable Energy Sources")
plt.show()