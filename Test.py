import csv
import random

n = 250
m = 250
sublist = ['101', '102', '103', '104']
# 1 List of subjects
subjects1 = ['105', '106']
subjects2 = ['107', '108']

# Generate numbers from 1 to 250 and associate each number with 4 random subjects from subjects1
number_subjects_mapping = {}

for number in range(1, n):
    selected_subjects = random.sample(subjects1, 2)
    number_subjects_mapping[number] = selected_subjects

# Add more subjects to the existing number_subjects_mapping for the next 250 rows
for number in range(n, n + m):
    selected_subjects = random.sample(subjects2, 2)
    number_subjects_mapping[number] = selected_subjects

csv_filename = 'test1.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(['Student number', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

    for number, subjects_list in number_subjects_mapping.items():
        csv_writer.writerow([number] + sublist + subjects_list)

print(f"Output saved to {csv_filename}")
