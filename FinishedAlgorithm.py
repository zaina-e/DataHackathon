import pandas as pd
import csv
from itertools import combinations
# File paths for the CSV files (use raw string literals)
csv_files = [
    r"C:\Users\zaina\OneDrive\Desktop\DataHackathon\batch1.csv",
    r"C:\Users\zaina\OneDrive\Desktop\DataHackathon\batch2.csv",
    r"C:\Users\zaina\OneDrive\Desktop\DataHackathon\batch3.csv",
]

# Load and concatenate the CSV files into a single DataFrame
try:
    student_data = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)
except Exception as e:
    error_message = str(e)

# Display the first few rows of the combined data to understand its structure
print(student_data.head() if 'student_data' in locals() else error_message)

# Check if student_data is not empty before proceeding
if 'student_data' in locals() and not student_data.empty:
    # Splitting the concatenated string into separate columns
    student_data_clean = student_data['S1;S2;S3;S4;S5;S6'].str.split(';', expand=True)

    # Renaming the columns for clarity
    student_data_clean.columns = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']

    # Converting subject columns to numeric for easier processing
    subject_columns = ['Subject1', 'Subject2', 'Subject3', 'Subject4', 'Subject5', 'Subject6']
    student_data_clean[subject_columns] = student_data_clean[subject_columns].apply(pd.to_numeric)

    # Displaying the cleaned data
    print(student_data_clean.head())

    # Counting the frequency of each subject across all students
    subject_frequencies = student_data_clean[subject_columns].stack().value_counts()

    # Converting the frequency data into a DataFrame for better readability
    subject_frequencies_df = subject_frequencies.to_frame(name='Frequency').reset_index()
    subject_frequencies_df.columns = ['Subject_Code', 'Frequency']

    # Display the frequency of each subject
    print(subject_frequencies_df)

from itertools import combinations
import numpy as np

# Defining the number of days for the exam period and maximum exams per day
exam_period_days = 16  # 2 weeks excluding weekends
max_exams_per_day = 1  # To minimize the number of exams per day
midterm_gap1 = 2 # Gap between midterms

# Subjects are divided into two groups based on their frequencies
large_subjects = subject_frequencies_df[subject_frequencies_df['Frequency'] > 600]['Subject_Code'].tolist()
small_subjects = subject_frequencies_df[subject_frequencies_df['Frequency'] <= 600]['Subject_Code'].tolist()



def has_conflict_corrected(student_row, subjects_on_day):
    return any(student_row[subject] in subjects_on_day for subject in subject_columns)

schedule = {day: [] for day in range(1, exam_period_days + 1)}

# Calculate the number of days needed for larger subjects
days_for_large_subjects = min(exam_period_days, len(large_subjects))
subjects_per_day_large = len(large_subjects) // days_for_large_subjects

days_for_small_subjects = min(exam_period_days, len(small_subjects))
subjects_per_day_small = len(small_subjects) // days_for_small_subjects


for i, subject in enumerate(large_subjects + small_subjects):
    day = (i * (midterm_gap1 + 1) % exam_period_days) + 1
    schedule[day].append(subject)
    

for day, subjects in schedule.items():
    print(day, subjects)

output_rows = []
for day, subjects in schedule.items():
    subjects_list = subjects if subjects is not None else []  # Replace None with an empty list
    output_rows.append([day] + subjects_list)

# Save the output to a CSV file without the title row
csv_filename = 'schedule3.csv'
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';')
    for row in output_rows:
        csv_writer.writerow(row )

print(f"Output saved to {csv_filename}")