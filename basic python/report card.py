def get_marks(name):
    subj_1 = int(input("What did you get in maths? "))    
    subj_2 = int(input("What did you get in science? "))    
    subj_3 = int(input("What did you get in english? "))    
    subj_4 = int(input("What did you get in hindi? "))    
    subj_5 = int(input("What did you get in spanish? "))    
    subj_6 = int(input("What did you get in history? "))    
    subj_7 = int(input("What did you get in geography? "))    

    marks_dict = {
        "math": subj_1, "science": subj_2, "english": subj_3,
        "hindi": subj_4, "spanish": subj_5, "history": subj_6, "geography": subj_7
    }
    avg = sum(marks_dict.values()) / len(marks_dict)
    print_grade(name, avg)
    return marks_dict, avg

def print_grade(name, avg):
    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "B+"
    elif avg >= 70:
        grade = "B-"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    elif avg >= 40:
        grade = "D-"
    else:
        grade = "F"
    print(f"{name}, you have an average of {avg:.2f}% so you get a {grade}.")

def main():
    num_students = int(input("How many students? "))
    all_students = {}

    for _ in range(num_students):
        name = input("\nWhat is your name? ")
        marks_dict, avg = get_marks(name)
        all_students[name] = {"marks": marks_dict, "avg": avg}

    topper = max(all_students, key=lambda x: all_students[x]["avg"])
    
    print("Results")
    for name, data in all_students.items():
        print(f"{name}: {data['avg']:.2f}%")
    
    print(f" Topper: {topper} with {all_students[topper]['avg']:.2f}%")

main()
