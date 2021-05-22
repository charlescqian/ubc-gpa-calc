import pandas as pd
import numpy as np

df = pd.read_csv('grades.csv')

gpa_dict = {
    "A+": 4,
    "A": 3.9,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2,
    "C-": 1.7,
    "D": 1,
    "F": 0
}

grade_point_sum = 0
total_credits = 0
for index, row in df.iterrows():
    letter_grade = row['Letter']
    num_credits = row['Credits Earned']

    if pd.notnull(letter_grade) and pd.notnull(num_credits):
        grade_point_sum += gpa_dict.get(letter_grade) * num_credits
        total_credits += num_credits

gpa = grade_point_sum / total_credits
print(f'GPA (Out of 4.0): {gpa:.2f}')
