import pandas as pd
from datetime import datetime

def process_student_data(input_file, output_file):
    data = pd.read_excel(input_file, header=None, engine='openpyxl')
    output_data = []
    header = ["Student Name", "Student ID"] + [f"Class {i} - Teacher {i}" for i in range(1, 9)]
    student_rows = data[data[2] == "Student:"].index
    for student_row in student_rows:
        student_name = data.iloc[student_row, 3]
        student_id = data.iloc[student_row + 1, 3]
        classes = []
        for i in range(8):
            class_row = student_row + 8 + i
            if class_row >= len(data):
                classes.append("")
                continue
            class_name = data.iloc[class_row, 4] if pd.notna(data.iloc[class_row, 4]) else ""
            teacher_name = data.iloc[class_row, 12] if pd.notna(data.iloc[class_row, 12]) else ""
            if class_name and teacher_name:
                classes.append(f"{class_name} - {teacher_name}")
            else:
                classes.append("")
        output_data.append([student_name, student_id] + classes)
    output_df = pd.DataFrame(output_data, columns=header)
    output_df.to_excel(output_file, index=False, engine="openpyxl")

input_file = r"C:\Users\Public\Projects\input.xlsx"  # Replace with the input file path
output_file = f"C:\\Users\\Public\\Projects\\output_{datetime.now().strftime('%Y%m%d')}.xlsx"  # Replace with the output file path

process_student_data(input_file, output_file)
print(f"Processed data has been written to {output_file}")
