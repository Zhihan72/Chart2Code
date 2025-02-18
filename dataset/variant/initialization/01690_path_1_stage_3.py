import matplotlib.pyplot as plt

technologies = ['Solar Power', 'Wind Energy', 'Hydroelectric', 'Geothermal', 'Biomass', 'Fusion Energy', 'Tidal Power']
shares = [30, 20, 15, 10, 10, 10, 5]
colors = ['#ffcc00', '#6699ff', '#66ff66', '#ff9966', '#ff66b3', '#b366ff', '#ff6666']
explode = (0.1, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    shares, 
    labels=technologies, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode, 
    wedgeprops={'width': 0.3}  # This makes it a donut chart
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