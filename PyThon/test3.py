import numpy as np
scores = np.array([
    [78,85,90],
    [88,79,92],
    [84,76,88],
    [90,93,94],
    [75,80,70]
])

# for idx,score in enumerate (scores):
#     current_average_score = round(np.average(score),2)
#     print(f"Student {idx+1} average score: {current_average_score}")

student_average = np.round(np.average(scores, 1),2)
print(f"Average of each student: {student_average}")
subject_average = np.round(np.average(scores, 0),2)
print(f"Average of each subject: {subject_average}")
highest_score_student = np.argmax(np.sum(scores, 1))+1
print(f"Student {highest_score_student} has the highest total score")

additional_score = 5
scores[:, -1] = scores[:, -1] + additional_score
print(scores)