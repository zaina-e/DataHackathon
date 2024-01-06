import csv
import random

a = 600
b = 400
sublist = ['101', '102', '103', '104']

# List of subjects
subjects_set1 = ['105', '106']
subjects_set2 = ['107', '108']

# Generate subject lists for subjects_set1 students
subject_lists_set1 = [random.sample(subjects_set1, 2) for _ in range(a)]

# Generate subject lists for subjects_set2 students
subject_lists_set2 = [random.sample(subjects_set2, 2) for _ in range(b)]

csv_filename = 'batch1.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(['Subject1', 'Subject2', 'Subject3', 'Subject4', 'Subject5', 'Subject6'])

    # Write information for subjects_set1 students
    for subjects_list in subject_lists_set1:
        csv_writer.writerow(sublist + subjects_list)

    # Write information for subjects_set2 students
    for subjects_list in subject_lists_set2:
        csv_writer.writerow(sublist + subjects_list)

print(f"Output saved to {csv_filename}")
