import matplotlib.pyplot as plt

clean_energy_sources = ['Solar Juice', 'Windy', 'Hydro', 'BioForce', 'Geo Power', 'Tidal Wave']
market_share = [35, 25, 20, 10, 7, 3]
single_color = '#66b3ff'  # Consistent color for all sections
explode = (0.1, 0, 0, 0, 0, 0)

def create_donut_pie(sources, market_share, color, explode):
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(
        market_share, labels=sources, autopct='%1.1f%%', startangle=140,
        colors=[color] * len(sources), explode=explode, wedgeprops=dict(edgecolor='none')
    )
    
    for text in texts:
        text.set_fontsize(9)

    for autotext in autotexts:
        autotext.set_fontsize(9)

    centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='none')
    ax.add_artist(centre_circle)

    plt.show()

def create_donut_comparison_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7))

    energy_types = ['Green Power', 'Fossil Fuels']
    energy_percentages = [55, 45]

    ax1.pie(
        market_share, labels=clean_energy_sources, autopct='%1.1f%%', startangle=140,
        colors=[single_color] * len(clean_energy_sources), explode=explode, wedgeprops=dict(edgecolor='none')
    )
    centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='none')
    ax1.add_artist(centre_circle)

    ax2.pie(
        energy_percentages, labels=energy_types, autopct='%1.1f%%', startangle=140,
        colors=[single_color, single_color], explode=(0.1, 0), wedgeprops=dict(edgecolor='none')
    )
    centre_circle_2 = plt.Circle((0, 0), 0.70, fc='white', edgecolor='none')
    ax2.add_artist(centre_circle_2)

    plt.show()

create_donut_pie(clean_energy_sources, market_share, single_color, explode)
create_donut_comparison_chart()