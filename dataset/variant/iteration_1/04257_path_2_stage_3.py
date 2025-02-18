import matplotlib.pyplot as plt
import squarify

energy_sources = [
    'Solar Power', 
    'Wind Power', 
    'Hydro Power', 
    'Biomass Energy'
]

contributions = [300, 450, 200, 100]

total_contribution = sum(contributions)
sizes = [c / total_contribution * 100 for c in contributions]

# Static colors for each energy source
colors = ['#8B4513', '#FFD700', '#7FFFD4', '#87CEFA']

fig, ax = plt.subplots(figsize=(14, 8))

squarify.plot(sizes=sizes, label=[f"{source}\n{size:.1f}%" for source, size in zip(energy_sources, sizes)],
              color=colors, alpha=0.8, edgecolor="white", linewidth=2, 
              text_kwargs={'fontsize': 10, 'weight': 'bold', 'color': 'white'})

plt.axis('off')

plt.show()