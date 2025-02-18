import matplotlib.pyplot as plt

years = ['2018', '2019', '2020', '2021', '2022']
emissions_na = [5900, 5800, 5700, 5600, 5500]
emissions_eu = [4300, 4200, 4100, 4000, 3900]
emissions_as = [17000, 17500, 18000, 18500, 19000]
emissions_af = [1300, 1400, 1500, 1600, 1700]
emissions_sa = [2000, 2100, 2200, 2300, 2400]

countries_na = ['USA', 'Canada', 'Mexico']
proportion_na = [80, 15, 5]

countries_eu = ['Germany', 'UK', 'France']
proportion_eu = [40, 30, 30]

countries_as = ['China', 'India', 'Japan']
proportion_as = [50, 30, 20]

countries_af = ['South Africa', 'Nigeria', 'Egypt']
proportion_af = [30, 25, 20]

countries_sa = ['Brazil', 'Argentina', 'Colombia']
proportion_sa = [50, 30, 20]

fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))

axs[0, 0].bar(years, emissions_na, color='red', alpha=0.7)
axs[0, 0].bar(years, emissions_eu, color='purple', alpha=0.7)
axs[0, 0].bar(years, emissions_as, color='blue', alpha=0.7)
axs[0, 0].bar(years, emissions_af, color='green', alpha=0.7)
axs[0, 0].bar(years, emissions_sa, color='brown', alpha=0.7)
axs[0, 0].set_title('Yearly CO2 Emissions by Continent (2018-2022)', fontsize=16)
axs[0, 0].set_xlabel('Year', fontsize=14)
axs[0, 0].set_ylabel('CO2 Emissions (Million Tons)', fontsize=14)

axs[1, 0].pie(proportion_na, labels=countries_na, autopct='%1.1f%%', colors=['pink', 'navajowhite', 'lightgreen'])
axs[1, 0].set_title('Proportion of CO2 Emissions in North America (2022)', fontsize=14)

axs[0, 1].pie(proportion_eu, labels=countries_eu, autopct='%1.1f%%', colors=['lightgrey', 'lightblue', 'sienna'])
axs[0, 1].set_title('Proportion of CO2 Emissions in Europe (2022)', fontsize=14)

axs[0, 2].pie(proportion_as, labels=countries_as, autopct='%1.1f%%', colors=['limegreen', 'lightgreen', 'lavender'])
axs[0, 2].set_title('Proportion of CO2 Emissions in Asia (2022)', fontsize=14)

axs[1, 1].pie(proportion_af, labels=countries_af, autopct='%1.1f%%', colors=['purple', 'violet', 'lightblue'])
axs[1, 1].set_title('Proportion of CO2 Emissions in Africa (2022)', fontsize=14)

axs[1, 2].pie(proportion_sa, labels=countries_sa, autopct='%1.1f%%', colors=['darkred', 'orangered', 'peru'])
axs[1, 2].set_title('Proportion of CO2 Emissions in South America (2022)', fontsize=14)

plt.tight_layout()
plt.show()