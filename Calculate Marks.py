def calculate_percentage(total_marks, num_subjects):
    return (total_marks / (num_subjects * 100)) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif 80 <= percentage < 90:
        return "A"
    elif 70 <= percentage < 80:
        return "B+"
    elif 60 <= percentage < 70:
        return "B"
    elif 50 <= percentage < 60:
        return "C"
    elif 40 <= percentage < 50:
        return "D"
    else:
        return "F"
def main():
    subjects = ["Maths", "Science", "Social Science", "English", "Hindi"]
    num_subjects = len(subjects)
    total_marks = 0

    for i, subject in enumerate(subjects, start=1):
        marks = float(input(f"Enter the marks obtained in {subject}: "))
        total_marks += marks

    percentage = calculate_percentage(total_marks, num_subjects)
    grade = calculate_grade(percentage)

    print("Percentage:", percentage)
    print("Grade:", grade)

if __name__ == "__main__":
    main()
