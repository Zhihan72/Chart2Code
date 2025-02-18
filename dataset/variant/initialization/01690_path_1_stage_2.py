import matplotlib.pyplot as plt

# Updated data with additional technologies
technologies = ['Solar Power', 'Wind Energy', 'Hydroelectric', 'Geothermal', 'Biomass', 'Fusion Energy', 'Tidal Power']
shares = [30, 20, 15, 10, 10, 10, 5]

# Updated colors for each sector
colors = ['#ffcc00', '#6699ff', '#66ff66', '#ff9966', '#ff66b3', '#b366ff', '#ff6666']

# Define explode to highlight the 'Solar Power' sector
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    shares, 
    labels=technologies, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode
)

# Customize the appearance
plt.setp(texts, size=10, weight='bold', color='white')
plt.setp(autotexts, size=12, weight='bold')

# Title and remove any additional styling
plt.title(
    'Technological Advancements in Renewable Energy - 2023\nGreenTech World', 
    fontsize=14, 
    weight='bold', 
    pad=20
)

# Display the chart
plt.show()