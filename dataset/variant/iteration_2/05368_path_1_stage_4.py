import matplotlib.pyplot as plt

institutions = ['Universities', 'Tech Companies', 'Research Institutions']
categories = ['Social Media', 'Work/Emails', 'Streaming', 'Research', 'Shopping']

data_by_institution = {
    "Universities": [40, 20, 15, 20, 5],
    "Tech Companies": [10, 50, 10, 25, 5],
    "Research Institutions": [10, 15, 5, 60, 10]
}

colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff6666', '#c2c2f0']

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{:.1f}%\n({:d})'.format(pct, val)
    return my_autopct

def plot_donut_chart(data, institution, categories, colors):
    fig, ax = plt.subplots(figsize=(9, 7), subplot_kw=dict(aspect="equal"))
    
    wedges, texts, autotexts = ax.pie(
        data,
        labels=categories,
        autopct=make_autopct(data),
        startangle=140,
        colors=colors,
        wedgeprops=dict(width=0.3, edgecolor='white'),
        textprops=dict(color='white', fontsize=9, fontweight='bold')
    )
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    
    ax.set_title(f"{institution}:\nInternet Usage Breakdown", fontsize=14, fontweight='bold')
    
    plt.tight_layout()

    plt.show()

for institution, data in data_by_institution.items():
    plot_donut_chart(data, institution, categories, colors)