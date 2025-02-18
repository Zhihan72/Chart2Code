import matplotlib.pyplot as plt
import numpy as np

clean_energy_sources = ['Solar Power', 'Wind Energy', 'Hydropower', 'Biomass Energy', 'Geothermal Energy', 'Tidal Energy']
market_share = [35, 25, 20, 10, 7, 3]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
explode = (0.1, 0, 0, 0, 0, 0)

def create_pie(sources, market_share, colors, explode):
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(
        market_share, labels=sources, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, wedgeprops=dict(edgecolor='none')
    )
    
    for text in texts:
        text.set_fontsize(9)

    for autotext in autotexts:
        autotext.set_fontsize(9)

    centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='none')
    fig.gca().add_artist(centre_circle)

    plt.show()

def create_comparison_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7))

    energy_types = ['Renewable', 'Non-Renewable']
    energy_percentages = [55, 45]

    ax1.pie(
        market_share, labels=clean_energy_sources, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, wedgeprops=dict(edgecolor='none')
    )

    centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='none')
    fig.gca().add_artist(centre_circle)

    ax2.pie(
        energy_percentages, labels=energy_types, autopct='%1.1f%%', startangle=140,
        colors=['#66b3ff', '#ff6666'], explode=(0.1, 0), wedgeprops=dict(edgecolor='none')
    )

    centre_circle_2 = plt.Circle((0, 0), 0.70, fc='white', edgecolor='none')
    fig.gca().add_artist(centre_circle_2)

    plt.show()

create_pie(clean_energy_sources, market_share, colors, explode)
create_comparison_chart()