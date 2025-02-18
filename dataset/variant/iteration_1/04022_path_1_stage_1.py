import matplotlib.pyplot as plt
import numpy as np

title = "Global Market Share of Clean Energy Sources in 2023"
subtitle = "A Comparative Breakdown"

clean_energy_sources = [
    'Solar Power',
    'Wind Energy',
    'Hydropower',
    'Biomass Energy',
    'Geothermal Energy',
    'Tidal Energy'
]

market_share = [35, 25, 20, 10, 7, 3]

colors = ['#99ff99', '#ff9999', '#ffb3e6', '#c2c2f0', '#ffcc99', '#66b3ff']
explode = (0.05, 0.1, 0, 0, 0, 0)

def create_pie(chart_title, sources, market_share, colors, explode):
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(
        market_share, labels=sources, autopct='%1.1f%%', startangle=90,
        colors=colors, explode=explode, shadow=True, wedgeprops=dict(linestyle='-', linewidth=1.5)
    )
    
    for text in texts:
        text.set_fontsize(10)
        text.set_color('black')

    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_color('blue')
    
    centre_circle = plt.Circle((0, 0), 0.65, fc='white', edgecolor='k')
    fig.gca().add_artist(centre_circle)
    
    ax.set_title(chart_title, fontsize=13, fontweight='regular', pad=20)

    ax.legend(wedges, sources, title="Energy Sources", loc="upper right", bbox_to_anchor=(1.1, 1), fontsize=9)

    plt.tight_layout()
    plt.show()

def create_comparison_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7))

    energy_types = ['Renewable', 'Non-Renewable']
    energy_percentages = [55, 45]

    wedges, texts, autotexts = ax1.pie(
        market_share, labels=clean_energy_sources, autopct='%1.1f%%', startangle=90,
        colors=colors, explode=explode, shadow=True, wedgeprops=dict(linestyle=':', linewidth=1.5)
    )
    
    for text in texts:
        text.set_fontsize(10)
        text.set_color('black')

    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_color('blue')
    
    centre_circle = plt.Circle((0, 0), 0.65, fc='white', edgecolor='k')
    fig.gca().add_artist(centre_circle)

    ax1.set_title("Clean Energy Sources", fontsize=11, fontweight='regular', pad=20)

    wedges, texts, autotexts = ax2.pie(
        energy_percentages, labels=energy_types, autopct='%1.1f%%', startangle=90,
        colors=['#66b3ff', '#ff6666'], explode=(0.05, 0.1), shadow=True, wedgeprops=dict(linestyle='-', linewidth=1.5)
    )
    
    for text in texts:
        text.set_fontsize(11)
        text.set_color('black')

    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_color('black')

    centre_circle_2 = plt.Circle((0, 0), 0.65, fc='white', edgecolor='k')
    fig.gca().add_artist(centre_circle_2)
    
    ax2.set_title("Renewable vs Non-Renewable", fontsize=11, fontweight='regular', pad=20)

    plt.tight_layout()
    plt.suptitle(f"{title}\n{subtitle}", fontsize=15, fontweight='bold', y=1.05)
    plt.show()

create_pie(title, clean_energy_sources, market_share, colors, explode)
create_comparison_chart()