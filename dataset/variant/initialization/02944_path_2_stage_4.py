import matplotlib.pyplot as plt

energy_distribution = [25, 20, 15, 10, 20, 10]
single_color = '#4682B4'  # Consistent single color for all data groups

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    energy_distribution, colors=[single_color]*len(energy_distribution),
    autopct='%1.1f%%', startangle=140, explode=(0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
)

plt.show()