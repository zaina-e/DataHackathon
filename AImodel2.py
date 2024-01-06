import pandas as pd
from itertools import combinations

# File paths for the CSV files (use raw string literals)
csv_files = [
    r"C:\Users\zaina\OneDrive\Desktop\DataHackathon\batch1.csv",
     r"C:\Users\Administrator\Desktop\Pyrhon\batch2.csv",
     r"C:\Users\Administrator\Desktop\Pyrhon\batch3.csv",
]

# Load and concatenate the CSV files into a single DataFrame
try:
    student_data = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)
except Exception as e:
    error_message = str(e)
    print(error_message)
    exit()

# Display the first few rows of the combined data to understand its structure
print(student_data.head())

# Check if student_data is not empty before proceeding
if not student_data.empty:
    # Splitting the concatenated string into separate columns
    student_data_clean = student_data['S1;S2;S3;S4;S5;S6'].str.split(';', expand=True)

    # Renaming the columns for clarity
    student_data_clean.columns = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']

    # Converting subject columns to numeric for easier processing
    subject_columns = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']
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

    import numpy as np

    # Defining the number of days for the exam period and maximum exams per day
    exam_period_days = 15  # 2 weeks excluding weekends
    max_exams_per_day = 1  # To minimize the number of exams per day

    # Subjects are divided into two groups based on their frequencies
    large_subjects = subject_frequencies_df[subject_frequencies_df['Frequency'] > 500]['Subject_Code'].tolist()
    small_subjects = subject_frequencies_df[subject_frequencies_df['Frequency'] <= 500]['Subject_Code'].tolist()

    # Correcting the conflict-checking function
    def has_conflict_corrected(student_row, subjects_on_day):
        return any(student_row[subject] in subjects_on_day for subject in subject_columns)

    # Initialize a schedule dictionary
    schedule = {day: [] for day in range(1, exam_period_days + 1)}

    # Schedule the larger subjects first, one per day
    for i, subject in enumerate(large_subjects):
        schedule[i + 1].append(subject)

    # Schedule the smaller subjects, checking for conflicts
    week1_subjects = []  # Subjects to be scheduled in week 1
    week2_subjects = []  # Subjects to be scheduled in week 2

    for subject in small_subjects:
        if subject in ['101', '102', '103', '104']:
            week2_subjects.append(subject)
        else:
            week1_subjects.append(subject)

    for subject in week1_subjects + week2_subjects:
        day = 1
        while day <= exam_period_days:
            # Check if adding this subject to the current day causes a conflict for too many students
            student_data_clean['Conflict'] = student_data_clean.apply(lambda row: has_conflict_corrected(row, schedule[day]), axis=1)
            if student_data_clean['Conflict'].sum() <= len(student_data_clean) // exam_period_days:
                schedule[day].append(subject)
                break
            day += 1

    # Convert schedule to a more readable format
    readable_schedule = {f"Day {day}": [f"Subject {subject}" for subject in subjects] for day, subjects in schedule.items()}

    print(readable_schedule)