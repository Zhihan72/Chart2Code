import matplotlib.pyplot as plt

# Years from 2000 to 2020
years = list(range(2000, 2021))

# Manually shuffled hypothetical average annual temperatures for Atlantis and El Dorado
temp_atlantis = [15.8, 15.4, 15.3, 16.0, 15.7, 16.4, 16.3, 16.7, 16.6, 17.0, 16.8, 17.5, 17.3, 17.8, 17.6, 18.0, 17.2, 18.3, 18.2, 18.7, 18.5]
temp_el_dorado = [17.8, 17.6, 17.5, 18.3, 18.0, 18.6, 18.1, 18.8, 18.5, 19.3, 19.0, 19.9, 19.1, 20.0, 20.2, 19.4, 19.7, 20.5, 20.4, 19.6, 20.2]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, temp_atlantis, label='Atlantis', marker='o', linestyle='-', color='blue', linewidth=2)
ax.plot(years, temp_el_dorado, label='El Dorado', marker='s', linestyle='--', color='red', linewidth=2)

plt.title('Average Annual Temperature Changes in Atlantis and El Dorado (2000-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)
plt.legend(title='Cities', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)

for i, (atl_temp, eld_temp) in enumerate(zip(temp_atlantis, temp_el_dorado)):
    ax.text(years[i], atl_temp + 0.1, f'{atl_temp:.1f}', ha='center', fontsize=9, color='blue')
    ax.text(years[i], eld_temp + 0.1, f'{eld_temp:.1f}', ha='center', fontsize=9, color='red')

plt.tight_layout()
plt.show()