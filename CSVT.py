import csv
import random
#low diversity 2 schedule, medium diversity same as low + 2 more schedules, high diversity medium diversity + 4 schedules

n = 500
sublist = ['101','102','103','104']
# 1 List of subjects
subjects = ['105', '106']

# Generate numbers from 1 to 100 and associate each number with 4 random subjects
number_subjects_mapping = {}

for number in range(1, n):
    # Randomly select 4 subjects for each number
    selected_subjects = random.sample(subjects, 2)
    
    # Associate the subjects with the number
    number_subjects_mapping[number] = selected_subjects

csv_filename = 'output1.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(['Student number', 'S1', 'S2', 'S3', 'S4', 'S5','S6'])

    for number, subjects_list in number_subjects_mapping.items():
        csv_writer.writerow([number] + sublist + subjects_list)
    
print(f"Output saved to {csv_filename}")

# 2 List of subjects
subjects2 = ['107', '108']

# Generate numbers from 1 to 100 and associate each number with 4 random subjects
number_subjects_mapping = {}

for number in range(1, n):
    # Randomly select 4 subjects for each number
    selected_subjects = random.sample(subjects2, 2)
    
    # Associate the subjects with the number
    number_subjects_mapping[number] = selected_subjects


csv_filename = 'output2.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(['Student number', 'S1', 'S2', 'S3', 'S4', 'S5','S6'])

    for number, subjects_list in number_subjects_mapping.items():
        csv_writer.writerow([number] + sublist + subjects_list)
    
print(f"Output saved to {csv_filename}")





# 3 List of subjects
subjects3 = ['105', '107']


number_subjects_mapping = {}

for number in range(1, n):
    
    selected_subjects = random.sample(subjects3, 2)
    
    # Associate the subjects with the number
    number_subjects_mapping[number] = selected_subjects

# Write the result to a CSV file
csv_filename = 'output3.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(['Student number', 'S1', 'S2', 'S3', 'S4', 'S5','S6'])

    for number, subjects_list in number_subjects_mapping.items():
        csv_writer.writerow([number] + sublist + subjects_list)
    
print(f"Output saved to {csv_filename}")





# 4 List of subjects
subjects4 = ['106', '108']


number_subjects_mapping = {}

for number in range(1, n):
    
    selected_subjects = random.sample(subjects4, 2)
    
    # Associate the subjects with the number
    number_subjects_mapping[number] = selected_subjects

# Write the result to a CSV file
csv_filename = 'output4.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(['Student number', 'S1', 'S2', 'S3', 'S4', 'S5','S6'])

    for number, subjects_list in number_subjects_mapping.items():
        csv_writer.writerow([number] + sublist + subjects_list)
    
print(f"Output saved to {csv_filename}")




# 5 List of subjects
subjects5 = ['105', '108']


number_subjects_mapping = {}

for number in range(1, n):
    
    selected_subjects = random.sample(subjects5, 2)
    
    # Associate the subjects with the number
    number_subjects_mapping[number] = selected_subjects

# Write the result to a CSV file
csv_filename = 'output5.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(['Student number', 'S1', 'S2', 'S3', 'S4', 'S5','S6'])

    for number, subjects_list in number_subjects_mapping.items():
        csv_writer.writerow([number] + sublist + subjects_list)
    
print(f"Output saved to {csv_filename}")


# 6 List of subjects
subjects6 = ['106', '107']


number_subjects_mapping = {}

for number in range(1, n):
    
    selected_subjects = random.sample(subjects6, 2)
    
    # Associate the subjects with the number
    number_subjects_mapping[number] = selected_subjects

# Write the result to a CSV file
csv_filename = 'output6.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(['Student number', 'S1', 'S2', 'S3', 'S4', 'S5','S6'])

    for number, subjects_list in number_subjects_mapping.items():
        csv_writer.writerow([number] + sublist + subjects_list)
    
print(f"Output saved to {csv_filename}")
        