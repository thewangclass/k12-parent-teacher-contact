from email_notification import email_parent
from data_manager import DataManager
import pandas as pd

FILE_NAME = 'data/grades_data.xlsx'
data_manager = DataManager()

xls = pd.ExcelFile(FILE_NAME)

for sheet in xls.sheet_names:
    student_list = data_manager.get_grades_data(FILE_NAME, sheet)

    for student in student_list:
        if student.grade_average < 70:
            email_parent(student)
