import matplotlib.pyplot as plt

years = ['2018', '2019', '2020', '2021', '2022']
demographics = ['Females', 'Males', 'Non-Conforming', 'Minorities', 'Misc']

data = {
    'Females': [31, 30, 36, 37, 39],
    'Males': [49, 47, 44, 42, 36],
    'Non-Conforming': [3, 5, 7, 8, 9],
    'Minorities': [14, 15, 19, 21, 20],
    'Misc': [2, 4, 3.5, 5, 4.8]
}

# Prepare data for boxplot
box_data = [data[group] for group in demographics]

fig, ax = plt.subplots(figsize=(10, 6))

ax.boxplot(box_data, vert=False, patch_artist=True,
           boxprops=dict(facecolor='#f58231', color='black'),
           whiskerprops=dict(color='black'),
           capprops=dict(color='black'),
           medianprops=dict(color='red'))

ax.set_title('InTechville Enrollment Trends (2018-2022)', fontsize=14, pad=15)
ax.set_xlabel('Participants (%)', fontsize=10)
ax.set_yticklabels(demographics)

plt.tight_layout()
plt.show()