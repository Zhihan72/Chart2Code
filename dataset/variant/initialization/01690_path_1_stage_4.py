import matplotlib.pyplot as plt

technologies = ['Solar Power', 'Wind Energy', 'Hydroelectric', 'Geothermal', 'Biomass', 'Fusion Energy', 'Tidal Power']
shares = [30, 20, 15, 10, 10, 10, 5]
single_color = '#66b3ff'  # Use a single color for all data groups
explode = (0.1, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    shares, 
    labels=technologies, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=[single_color] * len(technologies),  # Apply single color to all sectors
    explode=explode, 
    wedgeprops={'width': 0.3}
)

plt.setp(texts, size=10, weight='bold', color='white')
plt.setp(autotexts, size=12, weight='bold')

plt.title(
    'Technological Advancements in Renewable Energy - 2023\nGreenTech World', 
    fontsize=14, 
    weight='bold', 
    pad=20
)

plt.show()