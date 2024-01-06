import csv
import random

a = 250
b = 350
c = 150
d = 250
sublist = ['101', '102', '103', '104']

# List of subjects
subjects_set1 = ['105', '106', '107']
subjects_set2 = ['107', '108','105']
subjects_set3 = ['107', '105']
subjects_set4 = ['106', '108']

subject_lists_set1 = [random.sample(subjects_set1, 2) for _ in range(a)]

subject_lists_set2 = [random.sample(subjects_set1, 2) for _ in range(b)]

subject_lists_set3 = [random.sample(subjects_set2, 2) for _ in range(c)]

subject_lists_set4 = [random.sample(subjects_set2, 2) for _ in range(d)]

csv_filename = 'batch5.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(['Subject1', 'Subject2', 'Subject3', 'Subject4', 'Subject5', 'Subject6'])


    for subjects_list in subject_lists_set1:
        csv_writer.writerow(sublist + subjects_list)

  
    for subjects_list in subject_lists_set2:
        csv_writer.writerow(sublist + subjects_list)

    for subjects_list in subject_lists_set3:
        csv_writer.writerow(sublist + subjects_list)

    for subjects_list in subject_lists_set4:
        csv_writer.writerow(sublist + subjects_list)
        
print(f"Output saved to {csv_filename}")
