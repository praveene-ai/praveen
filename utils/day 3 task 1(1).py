import numpy as np
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

print("Marks:")
print(marks)

print("Shape:", marks.shape)
print("Data type:", marks.dtype)
print("Size:", marks.size)



print("\nFirst two students:")
print(marks[:2])

print("Last subject of first two students:")
print(marks[:2, -1])


student_avg = np.mean(marks, axis=1)
print("\nStudent averages:", np.round(student_avg, 2))


subject_avg = np.mean(marks, axis=0)
print("Subject averages:", np.round(subject_avg, 2))


grace_marks = marks + 5
print("\nMarks after adding grace marks:")
print(grace_marks)


weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks, weights)
print("\nWeighted scores:", weighted_scores)

# Reshape
numbers = np.arange(12)
reshaped = numbers.reshape(3, 4)

print("\nReshaped array:")
print(reshaped)
