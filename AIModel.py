import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

n = 500
sublist = ['101', '102', '103', '104']
subjects = ['105', '106']
csv_files = ['output1.csv', 'output2.csv', 'output3.csv', 'output4.csv', 'output5.csv', 'output6.csv']

# Load the data dictionary
data_dict = {}

for csv_file in csv_files:
    with open(csv_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            student_number = int(row[0])
            schedule = row[1:7]
            subjects = row[7:]
            data_dict[student_number] = {'schedule': schedule, 'subjects': subjects}

# Convert the data from the dictionary to numpy arrays for plotting
data = np.array([data_dict[student]['schedule'] for student in data_dict])
labels = np.array([data_dict[student]['subjects'] for student in data_dict])

# Plot the data before classification
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c='blue', label='Before Classification')
plt.xlabel('Subject 1')
plt.ylabel('Subject 2')
plt.title('Student Schedules - Before Classification')
plt.legend()
plt.show()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Initialize and train the KNN classifier
k = 3  # Number of neighbors to consider
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Plot the data after classification
plt.figure(figsize=(8, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c='red', label='After Classification')
plt.xlabel('Subject 1')
plt.ylabel('Subject 2')
plt.title('Student Schedules - After Classification (Accuracy: {:.2f})'.format(accuracy))
plt.legend()
plt.show()