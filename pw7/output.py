from input import get_ordinal_number

def display_mark_sheet(sorted_list):
    print("---------------------------------------------------")
    print("--------------------MARK SHEET---------------------")
    position = 1
    for student, gpa in sorted_list:
        ordinal_position = get_ordinal_number(position)
        print(f"{ordinal_position} | Student: {student.get_name()} | ID: {student.get_id()} | GPA: {gpa}")
        position += 1