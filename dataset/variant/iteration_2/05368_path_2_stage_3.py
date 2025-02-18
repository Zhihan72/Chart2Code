import matplotlib.pyplot as plt
import numpy as np

data_by_institution = {
    "Universities": [40, 20, 15, 20, 5],
    "Tech Companies": [10, 50, 10, 25, 5],
    "Hospitals": [5, 40, 5, 35, 15],
    "Government Offices": [5, 45, 5, 35, 10],
    "Research Institutions": [10, 15, 5, 60, 10],
    "Public Schools": [30, 20, 25, 15, 10]
}

single_color = ['#66b3ff']

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{:.1f}%\n({:d})'.format(pct, val)
    return my_autopct

def plot_pie_chart(data, color):
    fig, ax = plt.subplots(figsize=(9, 7), subplot_kw=dict(aspect="equal"))
    
    wedges, texts, autotexts = ax.pie(
        data,
        autopct=make_autopct(data),
        startangle=140,
        colors=color * len(data),
        pctdistance=0.8,
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
        textprops=dict(color='white', fontsize=9, fontweight='bold')
    )
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)

    plt.tight_layout()
    plt.show()

for institution, data in data_by_institution.items():
    plot_pie_chart(data, single_color)