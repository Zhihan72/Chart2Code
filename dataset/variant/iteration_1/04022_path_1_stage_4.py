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
    'Tidal Energy',
    'Nuclear Fusion'
]

market_share = [32, 23, 18, 10, 7, 3, 7]

new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
explode = (0.05, 0.1, 0, 0, 0, 0, 0.1)

def create_donut(chart_title, sources, market_share, colors, explode):
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(
        market_share, labels=sources, autopct='%1.1f%%', startangle=90,
        colors=colors, explode=explode, shadow=True, wedgeprops=dict(width=0.3, edgecolor='w')
    )
    
    ax.set_title(chart_title, fontsize=13, fontweight='regular', pad=20)
    ax.legend(wedges, sources, title="Energy Sources", loc="upper right", bbox_to_anchor=(1.1, 1), fontsize=9)

    plt.tight_layout()
    plt.show()

def create_comparison_donut_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7))

    energy_types = ['Renewable & Fusion', 'Non-Renewable']
    energy_percentages = [62, 38]

    ax1.pie(
        market_share, labels=clean_energy_sources, autopct='%1.1f%%', startangle=90,
        colors=new_colors, explode=explode, shadow=True, wedgeprops=dict(width=0.3, edgecolor='w')
    )
    ax1.set_title("Clean Energy Sources", fontsize=11, fontweight='regular', pad=20)

    ax2.pie(
        energy_percentages, labels=energy_types, autopct='%1.1f%%', startangle=90,
        colors=['#66b3ff', '#ff6666'], explode=(0.05, 0.1), shadow=True, wedgeprops=dict(width=0.3, edgecolor='w')
    )
    ax2.set_title("Renewable vs Non-Renewable", fontsize=11, fontweight='regular', pad=20)

    plt.tight_layout()
    plt.suptitle(f"{title}\n{subtitle}", fontsize=15, fontweight='bold', y=1.05)
    plt.show()

create_donut(title, clean_energy_sources, market_share, new_colors, explode)
create_comparison_donut_chart()